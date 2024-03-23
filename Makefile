# Global variables
USER != whoami
MAKE != which make
GIT != which git
PYTHON != which python
PDM != which pdm

# Package variables
PACKAGE_NAME := $(firstword $(shell $(PDM) show --name))
PACKAGE_VERSION := $(lastword $(shell $(PDM) show --version))

# Options
INSTALL_OPT :=
TEST_OPT := --doctest-modules --cov=src --cov-report=term-missing tests




help:  ## Show this help
	@echo "$(shell tput setaf 2)\n* Available targets\n$(shell tput sgr0)"

	@awk '/##/ && !/@awk/  {sub(/:/, "", $$1); comment_index=index($$0, "##"); print " " substr($$1, 0, comment_index) "\t" substr($$0, comment_index+2)}' $(MAKEFILE_LIST) | expand -t20

	@echo ""
	@echo "- You can pass options to override default befaviors by running: 'make OPT_A=... OPT_B=... TARGET'"
	@echo "- Run in dryrun mode: 'make -n TARGET'"
	@echo ""


info:  ## Show environment information, ref: https://www.cmcrossroads.com/article/dumping-every-makefile-variable
	$(info $(shell tput setaf 2)* Show environment information$(shell tput sgr0))
	@$(foreach V, $(sort $(.VARIABLES)), \
		$(if $(filter-out environment% default automatic,$(origin $V)), \
			$(info [$(origin $V)] $(shell tput setaf 4)$V$(shell tput sgr0)=$($V)) \
		) \
	)


sync: install  ## Sync project metadata with pyproject.toml
	$(PDM) run inv sync-meta


install: .venv  ## Install dependencies, Options:
##     INSTALL_OPT: options applied to "pdm install", default: $(INSTALL_OPT)
	$(info $(shell tput setaf 2)* Install dependencies $(shell tput sgr0))
	$(PDM) install $(INSTALL_OPT)


testing: .venv  ## Run unittest, Options:
##     TEST_OPT: options applied to "pytest", default: $(TEST_OPT)
	$(info $(shell tput setaf 2)* Run unittest $(shell tput sgr0))
	$(PDM) run pytest $(TEST_OPT)


clean:  ## Delete all files generated by building process
	$(info $(shell tput setaf 3)* Delete all files generated by building process $(shell tput sgr0))
	find . | grep -E "(\.coverage|\.pytest_cache|__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
	rm -rf dist


.venv:
	$(info $(shell tput setaf 2)* Create virtual environment $(shell tput sgr0))
	$(PYTHON) -m venv .venv


.PHONY: testing install clean info sync
