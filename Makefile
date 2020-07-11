update:
	cd qiskit-terra; git fetch upstream; git merge upstream/master; pip install -e .;
	cd qiskit-aqua; git fetch upstream; git merge upstream/master;; pip install -e .;
