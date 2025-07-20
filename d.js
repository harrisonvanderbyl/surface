const fs = require('fs');
const path = require('path');
const https = require('https');
const { URL } = require('url');

const BASE_URL = 'https://raw.githubusercontent.com/torvalds/linux/refs/heads/master/include/';
const BASEDTSIURL = 'https://raw.githubusercontent.com/torvalds/linux/refs/heads/master/arch/arm64/boot/dts/qcom/';
const OUTPUT_DIR = path.join(__dirname, 'include');
const downloaded = new Set();
const MAX_REDIRECTS = 5;

function fetchFileWithRedirects(url, redirects = 0) {
    return new Promise((resolve, reject) => {
        if (redirects > MAX_REDIRECTS) {
            return reject(new Error(`Too many redirects: ${url}`));
        }

        https.get(url, res => {
            if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
                const redirectUrl = new URL(res.headers.location, url).toString();
                console.log(`Redirecting to: ${redirectUrl}`);
                return resolve(fetchFileWithRedirects(redirectUrl, redirects + 1));
            }

            if (res.statusCode !== 200) {
                return reject(new Error(`HTTP ${res.statusCode} on ${url}`));
            }

            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(data));
        }).on('error', reject);
    });
}

async function saveFile(relPath, content) {
    const fullPath = path.join(OUTPUT_DIR, relPath);
    await fs.promises.mkdir(path.dirname(fullPath), { recursive: true });
    await fs.promises.writeFile(fullPath, content);
}

function parseIncludes(content) {
    const includes = [];
    const regex = /^\s*#\s*include\s*[<"](.+)[>"]/gm;
    let match;
    while ((match = regex.exec(content)) !== null) {
        includes.push(match[1]);
    }
    return includes;
}

async function downloadRecursive(relPath) {
    if (downloaded.has(relPath)) return;
    downloaded.add(relPath);
    var burl = BASE_URL;
    if (relPath.includes(".dtsi")) {
        burl = BASEDTSIURL;
    }
    const url = new URL(relPath, burl).toString();
    console.log(`Downloading: ${url}`);

    let content;
    try {
        content = await fetchFileWithRedirects(url);
    } catch (err) {
        console.warn(`Failed to fetch ${relPath}: ${err.message}`);
        return;
    }

    await saveFile(relPath, content);
    const includes = parseIncludes(content);

    for (const inc of includes) {
        if (!inc.includes('..') && !path.isAbsolute(inc)) {
            await downloadRecursive(inc);
        }
    }
}
// Entry point
(async () => {
    const rootHeader = 'x1p42100-crd.dts'; // start file
    content = fs.readFileSync(path.join(rootHeader), 'utf8');
     const includes = parseIncludes(content);

    for (const inc of includes) {
        // only follow includes inside the 'include' directory
        if (!inc.includes('..') && !path.isAbsolute(inc)) {
            await downloadRecursive(inc);
        }
    }
})();
