# Дмитрий, вот минимальный набор команд, чтобы закоммитить и залить (push) папку на GitHub. Делай в PowerShell/терминале внутри этой папки.
#
# #1) Если Git ещё НЕ включён в папке (первый раз)
import cd
import git

cd "C:\Users\Дмитро Антоненко\Documents\GitHub\BPC-PRG"
git init
git add .
git commit -m "test"
git branch -M main
git remote add origin https://github.com/slytherins-hub/exercise-7-monday-accelerometer-activity-DimonTheCloud.git
git push -u origin main
#2) Если Git уже включён и репозиторий уже привязан (у тебя сейчас так)
#
# #Каждый раз для нового ДЗ:
#
cd "C:\Users\Дмитро Антоненко\Documents\GitHub\BPC-PRG"
git add .
git commit -m ("smth")
git push
# Быстрые проверки
#
# посмотреть, что изменилось:
#
git status
#
# увидеть историю коммитов:
#
git log --oneline --max-count=10