#Note:before use of camelcase
# we must install pip install camelcase in terminal
#if you want uninstall camelcase then pip uninstall camelcase
import camelcase
camel = camelcase.CamelCase()#camelcase(package).CamelCase(class)
txt = "hello srinviasarao kunchala how are you"
print(camel.hump(txt)) #Title Case
print(txt.lower()) #lowecase
print(txt.upper()) #uppercase