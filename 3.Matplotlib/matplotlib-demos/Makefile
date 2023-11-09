PY = python

all: stacked_bar masked markevery barchart arctest style_sheets elements pandas histgram multihist streamplot pie

arctest:
	${PY} arctest.py > ./results/all-properties.txt

barchart:
	${PY} barchart.py

elements:
	${PY} elements.py

histgram:
	${PY} histgram.py

stacked_bar:
	${PY} stacked_bar.py

masked:
	${PY} masked.py

markevery:
	${PY} markevery.py

multihist:
	${PY} multihist.py

pandas:
	${PY} pd.py

pie:
	${PY} pie.py

streamplot:
	${PY} streamplot.py

style_sheets:
	${PY} style_sheets.py > ./results/all-styles.txt

clean:
	rm ./figures/* ./results/* -rf

rebuild: clean all