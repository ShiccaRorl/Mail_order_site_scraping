# -*- mode: python -*-
# filename = Compile.spec

a = Analysis(['pythonファイル名'],
             pathex=['スクリプトがあるPATH'],
             datas=[('./data/logo.png','DATA'),('./data/sample01.png','DATA'),('./data/sample02.png','DATA')],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Main',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='アイコンファイル')
app = BUNDLE(exe,
             name='実行ファイル名',
             icon='アイコンファイル')