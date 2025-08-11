savedcmd_include/generated/vdso-offsets.h := nm arch/arm64/kernel/vdso/vdso.so.dbg | ./arch/arm64/kernel/vdso/gen_vdso_offsets.sh | LC_ALL=C sort > include/generated/vdso-offsets.h
