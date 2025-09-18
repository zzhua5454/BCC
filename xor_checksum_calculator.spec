# -*- mode: python ; coding: utf-8 -*-

# 确保中文显示正常
import sys
if sys.platform == 'win32':
    import _locale
    _locale._getdefaultlocale = lambda *args: ['zh_CN', 'utf8']

a = Analysis(
    ['xor_checksum_calculator.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='异或校验和计算',  # 将可执行文件名改为中文
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['xor3.ico'],
)
