@echo off
pushd %~dp0

::VSCODE����ϵͳĬ��·��
REM set "CodeData=%appdata%\Code\"

REM :: ����Դ�ļ����ڵ�ϵͳ·��
REM set "BACK0=%CodeData%\Backups"
REM set "STORAGE0=%CodeData%\storage.json"
REM set "KEYSET0=%CodeData%\User\keybindings.json"

REM :: �����������ļ���·��
REM set "BACK1=%~dp0.vscode\Backups"
REM set "STORAGE1=%~dp0.vscode\storage.json"
REM set "KEYSET1=%~dp0.vscode\keybindings.json"

REM :: ������������δ�������ݵ�������
REM rd /S /Q "%BACK0%"
REM REM del /F /Q "%STORAGE0%"
REM del /F /Q "%KEYSET0%"

REM :: ������
REM mklink /D "%BACK0%" "%BACK1%"
REM REM mklink /H "%STORAGE0%" "%STORAGE1%"
REM mklink /H "%KEYSET0%" "%KEYSET1%"


set "���Ŀ¼=.vscode\extensions"
set "�û�����Ŀ¼=.vscode\Code"

code --user-data-dir %�û�����Ŀ¼% .

pause
exit
