class ACPIDSLParser {
    constructor() {
        this.devices = [];
        this.regulators = [];
        this.gpios = [];
        this.interrupts = [];
        this.clocks = [];
        this.powerDomains = [];
        this.memoryRegions = [];
        this.dmaChannels = [];
        this.currentScope = [];
    }

    /**
     * Main parsing function
     * @param {string} dslContent - The ACPI DSL file content
     * @returns {Object} Parsed hardware components
     */
    parse(dslContent) {
        this.reset();
        const lines = dslContent.split('\n');
        
        for (let i = 0; i < lines.length; i++) {
            const line = lines[i].trim();
            if (!line || line.startsWith('//') || line.startsWith('/*')) continue;
            
            this.parseLine(line, i, lines);
        }
        
        return this.getResults();
    }

    reset() {
        this.devices = [];
        this.regulators = [];
        this.gpios = [];
        this.interrupts = [];
        this.clocks = [];
        this.powerDomains = [];
        this.memoryRegions = [];
        this.dmaChannels = [];
        this.currentScope = [];
    }

    parseLine(line, lineNum, allLines) {
        // Parse device definitions
        if (this.isDeviceDefinition(line)) {
            this.parseDevice(line, lineNum, allLines);
        }
        
        // Parse scope changes
        if (line.includes('Scope (')) {
            this.parseScope(line);
        }
        
        // Parse method definitions that might contain hardware info
        if (line.includes('Method (')) {
            this.parseMethod(line, lineNum, allLines);
        }
        
        // Parse resource templates
        if (line.includes('ResourceTemplate')) {
            this.parseResourceTemplate(lineNum, allLines);
        }
        
        // Parse power resource definitions
        if (line.includes('PowerResource')) {
            this.parsePowerResource(line, lineNum, allLines);
        }
        
        // Parse external references
        if (line.includes('External (')) {
            this.parseExternal(line);
        }
    }

    isDeviceDefinition(line) {
        return line.includes('Device (') || line.includes('Device(');
    }

    parseDevice(line, lineNum, allLines) {
        const deviceMatch = line.match(/Device\s*\(\s*([A-Z0-9_]+)\s*\)/);
        if (!deviceMatch) return;

        const deviceName = deviceMatch[1];
        const device = {
            name: deviceName,
            fullPath: this.getFullPath(deviceName),
            type: 'device',
            properties: {},
            resources: [],
            methods: [],
            children: [],
            lineNumber: lineNum
        };

        // Parse device block
        const deviceBlock = this.extractBlock(lineNum, allLines);
        this.parseDeviceBlock(device, deviceBlock);
        
        this.devices.push(device);
    }

    parseDeviceBlock(device, block) {
        for (let i = 0; i < block.length; i++) {
            const line = block[i].trim();
            
            // Parse _HID (Hardware ID)
            if (line.includes('_HID')) {
                device.properties.hid = this.extractQuotedValue(line) || this.extractValue(line);
            }
            
            // Parse _CID (Compatible ID)
            if (line.includes('_CID')) {
                device.properties.cid = this.extractQuotedValue(line) || this.extractValue(line);
            }
            
            // Parse _UID (Unique ID)
            if (line.includes('_UID')) {
                device.properties.uid = this.extractValue(line);
            }
            
            // Parse _ADR (Address)
            if (line.includes('_ADR')) {
                device.properties.address = this.extractHexValue(line);
            }
            
            // Parse _STA (Status)
            if (line.includes('_STA')) {
                device.properties.status = this.extractHexValue(line);
            }
            
            // Parse _CRS (Current Resource Settings)
            if (line.includes('_CRS')) {
                const resourceBlock = this.extractMethodBlock(i, block);
                device.resources = this.parseResourceBlock(resourceBlock);
                this.categorizeResources(device.resources);
            }
            
            // Parse other important methods
            this.parseDeviceMethods(device, line, i, block);
        }
    }

    parseResourceBlock(block) {
        const resources = [];
        
        for (const line of block) {
            // Parse I/O resources
            if (line.includes('IO (')) {
                resources.push(this.parseIOResource(line));
            }
            
            // Parse Memory resources
            if (line.includes('Memory32Fixed') || line.includes('Memory32')) {
                resources.push(this.parseMemoryResource(line));
            }
            
            // Parse IRQ resources
            if (line.includes('IRQ (') || line.includes('Interrupt (')) {
                resources.push(this.parseInterruptResource(line));
            }
            
            // Parse GPIO resources
            if (line.includes('GpioIo') || line.includes('GpioInt')) {
                resources.push(this.parseGPIOResource(line));
            }
            
            // Parse I2C resources
            if (line.includes('I2cSerialBus')) {
                resources.push(this.parseI2CResource(line));
            }
            
            // Parse SPI resources
            if (line.includes('SpiSerialBus')) {
                resources.push(this.parseSPIResource(line));
            }
            
            // Parse DMA resources
            if (line.includes('DMA (')) {
                resources.push(this.parseDMAResource(line));
            }
            
            // Parse Clock resources
            if (line.includes('Clock (')) {
                resources.push(this.parseClockResource(line));
            }
        }
        
        return resources;
    }

    parseIOResource(line) {
        const match = line.match(/IO\s*\(\s*(\w+),\s*0x([0-9A-Fa-f]+),\s*0x([0-9A-Fa-f]+),\s*0x([0-9A-Fa-f]+),\s*0x([0-9A-Fa-f]+)/);
        if (match) {
            return {
                type: 'io',
                decode: match[1],
                minAddress: parseInt(match[2], 16),
                maxAddress: parseInt(match[3], 16),
                alignment: parseInt(match[4], 16),
                length: parseInt(match[5], 16)
            };
        }
        return { type: 'io', raw: line };
    }

    parseMemoryResource(line) {
        const match = line.match(/Memory32Fixed\s*\(\s*(\w+),\s*0x([0-9A-Fa-f]+),\s*0x([0-9A-Fa-f]+)/);
        if (match) {
            return {
                type: 'memory',
                readWrite: match[1],
                baseAddress: parseInt(match[2], 16),
                length: parseInt(match[3], 16)
            };
        }
        return { type: 'memory', raw: line };
    }

    parseInterruptResource(line) {
        const irqMatch = line.match(/IRQ\s*\(\s*([^)]+)\)\s*\{\s*(\d+)\s*\}/);
        const intMatch = line.match(/Interrupt\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+)(?:,\s*([^,]+))?\)\s*\{\s*0x([0-9A-Fa-f]+)\s*\}/);
        const intRawMatch = line.match(/Interrupt\s*\((.*)/);
        
        if (irqMatch) {
            return {
                type: 'interrupt',
                mode: 'legacy',
                flags: irqMatch[1].split(',').map(f => f.trim()),
                number: parseInt(irqMatch[2])
            };
        } else if (intMatch) {
            return {
                type: 'interrupt',
                mode: 'extended',
                resourceType: intMatch[1].trim(),
                level: intMatch[2].trim(),
                polarity: intMatch[3].trim(),
                sharing: intMatch[4].trim(),
                wake: intMatch[5] ? intMatch[5].trim() : undefined,
                number: parseInt(intMatch[6], 16)
            };
        } else if (intRawMatch) {
            const rawParts = intRawMatch[1].split(',').map(p => p.trim());
            const numberMatch = line.match(/\{\s*0x([0-9A-Fa-f]+)\s*\}/);
            return {
                type: 'interrupt',
                mode: 'extended',
                resourceType: rawParts[0],
                level: rawParts[1],
                polarity: rawParts[2],
                sharing: rawParts[3],
                wake: rawParts[4],
                number: numberMatch ? parseInt(numberMatch[1], 16) : undefined,
                raw: intRawMatch[1].trim()
            };
        }
        return { type: 'interrupt', raw: line };
    }

    parseGPIOResource(line) {
        const gpioMatch = line.match(/(GpioIo|GpioInt)\s*\(\s*([^)]+)\)/);
        if (gpioMatch) {
            const flags = gpioMatch[2].split(',').map(f => f.trim());
            const gpio = {
                type: 'gpio',
                function: gpioMatch[1].toLowerCase(),
                sharing: flags[0],
                pull: flags[1],
                pinConfig: flags[2],
                pinNumber: flags[3] ? parseInt(flags[3], 16) : undefined,
                activeLevel: flags[4],
                debounce: flags[5] ? parseInt(flags[5], 16) : undefined,
                vendorData: flags.slice(6).join(', ')
            };
            this.gpios.push(gpio);
            return gpio;
        }
        const gpioRawMatch = line.match(/(GpioIo|GpioInt)\s*\((.*)/);
        if (gpioRawMatch) {
            const rawFlags = gpioRawMatch[2].split(',').map(f => f.trim());
            return {
                type: 'gpio',
                function: gpioRawMatch[1].toLowerCase(),
                sharing: rawFlags[0],
                pull: rawFlags[1],
                pinConfig: rawFlags[2],
                pinNumber: rawFlags[3] ? parseInt(rawFlags[3], 16) : undefined,
                activeLevel: rawFlags[4],
                raw: gpioRawMatch[2].trim()
            };
        }
        const simplifiedGpioMatch = line.match(/(GpioIo|GpioInt)\s*\(\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*([^,]+)/);
        if (simplifiedGpioMatch) {
            return {
                type: 'gpio',
                function: simplifiedGpioMatch[1].toLowerCase(),
                sharing: simplifiedGpioMatch[2],
                pull: simplifiedGpioMatch[3],
                pinConfig: simplifiedGpioMatch[4],
                pinNumber: parseInt(simplifiedGpioMatch[5], 16),
                activeLevel: simplifiedGpioMatch[6],
                raw: line.trim()
            };
        }
        return { type: 'gpio', raw: line };
    }

    parseI2CResource(line) {
        const match = line.match(/I2cSerialBusV2?\s*\(\s*0x([0-9A-Fa-f]+),\s*([^,]+),\s*0x([0-9A-Fa-f]+)/);
        if (match) {
            return {
                type: 'i2c',
                address: parseInt(match[1], 16),
                mode: match[2].trim(),
                speed: parseInt(match[3], 16)
            };
        }
        return { type: 'i2c', raw: line };
    }

    parseSPIResource(line) {
        const match = line.match(/SpiSerialBus\s*\(\s*(\d+),\s*([^,]+),\s*(\d+),\s*(\d+),\s*([^,]+),\s*([^,]+),\s*([^,]+),\s*"([^"]+)"/);
        if (match) {
            return {
                type: 'spi',
                chipSelect: parseInt(match[1]),
                polarity: match[2].trim(),
                phase: parseInt(match[3]),
                speed: parseInt(match[4]),
                bitsPerWord: match[5].trim(),
                mode: match[6].trim(),
                sharing: match[7].trim(),
                controller: match[8]
            };
        }
        return { type: 'spi', raw: line };
    }

    parseDMAResource(line) {
        const match = line.match(/DMA\s*\(\s*([^,]+),\s*([^,]+),\s*([^)]+)\)\s*\{\s*(\d+)\s*\}/);
        if (match) {
            const dma = {
                type: 'dma',
                compatibility: match[1].trim(),
                busmaster: match[2].trim(),
                transfer: match[3].trim(),
                channel: parseInt(match[4])
            };
            this.dmaChannels.push(dma);
            return dma;
        }
        return { type: 'dma', raw: line };
    }

    parsePowerResource(line, lineNum, allLines) {
        const match = line.match(/PowerResource\s*\(\s*([A-Z0-9_]+),\s*0x([0-9A-Fa-f]+),\s*0x([0-9A-Fa-f]+)\)/);
        if (match) {
            const regulator = {
                type: 'regulator',
                name: match[1],
                systemLevel: parseInt(match[2], 16),
                resourceOrder: parseInt(match[3], 16),
                methods: [],
                fullPath: this.getFullPath(match[1])
            };
            
            const block = this.extractBlock(lineNum, allLines);
            this.parsePowerMethods(regulator, block);
            this.regulators.push(regulator);
        }
    }

    parsePowerMethods(regulator, block) {
        for (let i = 0; i < block.length; i++) {
            const line = block[i].trim();
            if (line.includes('Method (_ON') || line.includes('Method (_OFF') || line.includes('Method (_STA')) {
                const methodName = line.match(/Method\s*\(\s*([^,]+)/)?.[1];
                if (methodName) {
                    const methodBlock = this.extractMethodBlock(i, block);
                    regulator.methods.push({
                        name: methodName,
                        operations: this.parseMethodOperations(methodBlock)
                    });
                }
            }
        }
    }

    parseDeviceMethods(device, line, index, block) {
        const methodPatterns = [
            '_PS0', '_PS3', '_ON_', '_OFF', '_RST', '_DSM',
            '_DEP', '_PR0', '_PR3', '_PSC', '_PSW'
        ];
        
        for (const pattern of methodPatterns) {
            if (line.includes(pattern)) {
                const methodBlock = this.extractMethodBlock(index, block);
                device.methods.push({
                    name: pattern,
                    operations: this.parseMethodOperations(methodBlock)
                });
                break;
            }
        }
    }

    parseClockResource(line) {
        const match = line.match(/Clock\s*\(\s*([^,]+),\s*(\d+)\s*\)/);
        if (match) {
            const clock = {
                type: 'clock',
                name: match[1].trim(),
                frequency: parseInt(match[2])
            };
            this.clocks.push(clock);
            return clock;
        }
        return { type: 'clock', raw: line };
    }

    parseMethodOperations(methodBlock) {
        const operations = [];
        for (const line of methodBlock) {
            // Look for register operations, GPIO operations, etc.
            if (line.includes('Store (') || line.includes('And (') || line.includes('Or (')) {
                operations.push({ type: 'register_op', code: line.trim() });
            }
            if (line.includes('Sleep (')) {
                const delay = line.match(/Sleep\s*\(\s*(\d+)/)?.[1];
                operations.push({ type: 'delay', value: delay ? parseInt(delay) : 0 });
            }
        }
        return operations;
    }

    categorizeResources(resources) {
        for (const resource of resources) {
            switch (resource.type) {
                case 'interrupt':
                    this.interrupts.push(resource);
                    break;
                case 'memory':
                    this.memoryRegions.push(resource);
                    break;
                case 'gpio':
                    // Already handled in parseGPIOResource
                    break;
                case 'dma':
                    // Already handled in parseDMAResource
                    break;
            }
        }
    }

    parseScope(line) {
        const match = line.match(/Scope\s*\(\s*([^)]+)\)/);
        if (match) {
            this.currentScope.push(match[1].replace(/\\/g, '/'));
        }
    }

    parseExternal(line) {
        const match = line.match(/External\s*\(\s*([^,]+),\s*([^)]+)\)/);
        if (match) {
            // Track external references that might be regulators or clocks
            const extRef = {
                name: match[1].replace(/"/g, '').replace(/\\/g, '/'),
                type: match[2].trim()
            };
            
            if (extRef.type.includes('PowerResource') || extRef.name.includes('PWR')) {
                this.regulators.push({
                    type: 'regulator',
                    name: this.extractName(extRef.name),
                    external: true,
                    fullPath: extRef.name
                });
            }
        }
    }

    parseMethod(line, lineNum, allLines) {
        const methodMatch = line.match(/Method\s*\(\s*([^,]+)/);
        if (methodMatch) {
            const methodName = methodMatch[1];
            const methodBlock = this.extractMethodBlock(lineNum, allLines);
            const operations = this.parseMethodOperations(methodBlock);
            
            // You might want to store this method information somewhere
            // For now, we'll just log it
            console.log(`Parsed method: ${methodName}`);
            console.log(`Operations:`, operations);
        }
    }

    parseResourceTemplate(lineNum, allLines) {
        const resourceBlock = this.extractMethodBlock(lineNum, allLines);
        const resources = this.parseResourceBlock(resourceBlock);
        
        // You might want to store or process these resources
        console.log('Parsed ResourceTemplate:');
        console.log(resources);
        
        return resources;
    }

    extractBlock(startLine, allLines) {
        const block = [];
        let braceCount = 0;
        let started = false;
        
        for (let i = startLine; i < allLines.length; i++) {
            const line = allLines[i];
            if (line.includes('{')) {
                started = true;
                braceCount += (line.match(/\{/g) || []).length;
            }
            if (line.includes('}')) {
                braceCount -= (line.match(/\}/g) || []).length;
            }
            
            if (started) {
                block.push(line);
                if (braceCount === 0) break;
            }
        }
        
        return block;
    }

    extractMethodBlock(startIndex, parentBlock) {
        const block = [];
        let braceCount = 0;
        let started = false;
        
        for (let i = startIndex; i < parentBlock.length; i++) {
            const line = parentBlock[i];
            if (line.includes('{')) {
                started = true;
                braceCount += (line.match(/\{/g) || []).length;
            }
            if (line.includes('}')) {
                braceCount -= (line.match(/\}/g) || []).length;
            }
            
            if (started) {
                block.push(line);
                if (braceCount === 0) break;
            }
        }
        
        return block;
    }

    extractQuotedValue(line) {
        const match = line.match(/"([^"]+)"/);
        return match ? match[1] : null;
    }

    extractValue(line) {
        const match = line.match(/,\s*([^,\s)]+)/);
        return match ? match[1] : null;
    }

    extractHexValue(line) {
        const match = line.match(/0x([0-9A-Fa-f]+)/);
        return match ? parseInt(match[1], 16) : null;
    }

    extractName(path) {
        return path.split('/').pop() || path;
    }

    getFullPath(name) {
        if (this.currentScope.length > 0) {
            return this.currentScope.join('/') + '/' + name;
        }
        return name;
    }

    getResults() {
        return {
            devices: this.devices,
            regulators: this.regulators,
            gpios: this.gpios,
            interrupts: this.interrupts,
            clocks: this.clocks,
            powerDomains: this.powerDomains,
            memoryRegions: this.memoryRegions,
            dmaChannels: this.dmaChannels,
            summary: {
                totalDevices: this.devices.length,
                totalRegulators: this.regulators.length,
                totalGPIOs: this.gpios.length,
                totalInterrupts: this.interrupts.length,
                totalMemoryRegions: this.memoryRegions.length,
                totalDMAChannels: this.dmaChannels.length
            }
        };
    }

    /**
     * Generate a basic DTS structure from parsed data
     * @returns {string} Device Tree Source content
     */
    generateDTS() {
        let dts = '/dts-v1/;\n\n';
        dts += '/ {\n';
        dts += '    model = "ACPI Converted Device Tree";\n';
        dts += '    compatible = "acpi-dt";\n';
        dts += '    #address-cells = <2>;\n';
        dts += '    #size-cells = <2>;\n\n';

        // Add regulators
        if (this.regulators.length > 0) {
            dts += '    regulators {\n';
            for (const reg of this.regulators) {
                dts += `        ${reg.name.toLowerCase()}: ${reg.name.toLowerCase()}-regulator {\n`;
                dts += '            compatible = "regulator-fixed";\n';
                dts += `            regulator-name = "${reg.name}";\n`;
                if (reg.methods && reg.methods.length > 0) {
                    dts += '            /* ACPI power methods available */\n';
                }
                dts += '        };\n';
            }
            dts += '    };\n\n';
        }

        // Add devices
        for (const device of this.devices) {
            if (device.properties.hid) {
                const nodeName = device.name.toLowerCase().replace(/_/g, '-');
                dts += `    ${nodeName}@`;
                
                if (device.properties.address) {
                    dts += device.properties.address.toString(16);
                } else {
                    dts += '0';
                }
                
                dts += ' {\n';
                dts += `        compatible = "${device.properties.hid}";\n`;
                
                if (device.properties.cid) {
                    dts += `        /* Compatible ID: ${device.properties.cid} */\n`;
                }
                
                if (device.properties.address) {
                    dts += `        reg = <0 0x${device.properties.address.toString(16)} 0 0x1000>;\n`;
                }

                // Add resources
                const interrupts = device.resources.filter(r => r.type === 'interrupt');
                if (interrupts.length > 0) {
                    dts += '        interrupts =\n';
                    for (const interrupt of interrupts) {
                        if (interrupt.mode === 'legacy') {
                            dts += `            <${interrupt.number} ${interrupt.flags.join(' ')}>;\n`;
                        } else if (interrupt.mode === 'extended') {
                            if (interrupt.number !== undefined) {
                                dts += `            <${interrupt.number} ${interrupt.resourceType} ${interrupt.level} ${interrupt.polarity} ${interrupt.sharing}`;
                                if (interrupt.wake) {
                                    dts += ` ${interrupt.wake}`;
                                }
                                dts += '>;\n';
                            } else {
                                dts += `            /* Raw interrupt data: ${interrupt.raw} */\n`;
                            }
                        }
                    }
                }

                const gpios = device.resources.filter(r => r.type === 'gpio');
                if (gpios.length > 0) {
                    for (let i = 0; i < gpios.length; i++) {
                        const gpio = gpios[i];
                        if (gpio.pinNumber !== undefined && gpio.activeLevel !== undefined) {
                            dts += `        gpio-${gpio.function} = <&gpio ${gpio.pinNumber} (${gpio.activeLevel})>;\n`;
                        } else {
                            dts += `        /* Raw GPIO data: ${gpio.raw} */\n`;
                        }
                    }
                }

                const i2cResources = device.resources.filter(r => r.type === 'i2c');
                if (i2cResources.length > 0) {
                    for (const i2c of i2cResources) {
                        if (i2c.address !== undefined && i2c.speed !== undefined) {
                            dts += `        i2c-address = <0x${i2c.address.toString(16)}>;\n`;
                            dts += `        clock-frequency = <${i2c.speed}>;\n`;
                        } else {
                            dts += `        /* Raw I2C data: ${i2c.raw} */\n`;
                        }
                    }
                }

                dts += '        status = "okay";\n';
                dts += '    };\n\n';
            }
        }

        dts += '};\n';
        return dts;
    }

    /**
     * Export results in JSON format
     * @returns {string} JSON representation of parsed data
     */
    exportJSON() {
        return JSON.stringify(this.getResults(), null, 2);
    }

    /**
     * Export results in a detailed report format
     * @returns {string} Human-readable report
     */
    exportReport() {
        const results = this.getResults();
        let report = 'ACPI DSL to DTS Conversion Report\n';
        report += '================================\n\n';
        
        report += `Total Devices Found: ${results.summary.totalDevices}\n`;
        report += `Total Regulators: ${results.summary.totalRegulators}\n`;
        report += `Total GPIO Pins: ${results.summary.totalGPIOs}\n`;
        report += `Total Interrupts: ${results.summary.totalInterrupts}\n`;
        report += `Total Memory Regions: ${results.summary.totalMemoryRegions}\n`;
        report += `Total DMA Channels: ${results.summary.totalDMAChannels}\n\n`;

        if (results.devices.length > 0) {
            report += 'DEVICES:\n--------\n';
            for (const device of results.devices) {
                report += `${device.name} (${device.fullPath})\n`;
                if (device.properties.hid) report += `  HID: ${device.properties.hid}\n`;
                if (device.properties.cid) report += `  CID: ${device.properties.cid}\n`;
                if (device.properties.address) report += `  Address: 0x${device.properties.address.toString(16)}\n`;
                if (device.resources.length > 0) {
                    report += `  Resources: ${device.resources.length} items\n`;
                }
                report += '\n';
            }
        }

        return report;
    }
}

// command line interface for quick testing
if (require.main === module) {
    const fs = require('fs');
    const path = require('path');

    const dslFilePath = process.argv[2];
    if (!dslFilePath || !fs.existsSync(dslFilePath)) {
        console.error('Usage: node dst-dsl.js <path_to_acpi_dsl_file>');
        process.exit(1);
    }

    const dslContent = fs.readFileSync(dslFilePath, 'utf8');
    const parser = new ACPIDSLParser();
    
    const results = parser.parse(dslContent);
    console.log('Parsed Results:', JSON.stringify(results, null, 2));
    
    // Generate DTS
    const dtsContent = parser.generateDTS();
    console.log('Generated DTS:\n', dtsContent);
}
