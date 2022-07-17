build:
	easycython list_sum_cy.py
	easycython *.pyx


clean:
	@echo "Passando a vassoura"
	rm -rf __pycache__
	rm -f *.so
	rm -f *.c
	rm -f *.pyd
	rm -rf build
	rm -f *.html
	rm -f prof*
