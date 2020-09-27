ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

all:
> pyside2-uic src/UI/main.ui -o src/UI/main.py
> pyside2-rcc src/UI/Images.qrc -o src/Images_rc.py
