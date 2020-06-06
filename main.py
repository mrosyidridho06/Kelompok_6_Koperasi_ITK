from view.win import mainwin
from view.login import Login
import sys



main = mainwin()
main.show()
sys.exit(main.app.exec_())