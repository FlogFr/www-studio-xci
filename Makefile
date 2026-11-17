# Local preview through Docker, with the same gems as the GitHub Pages build.
# Gems are cached in the `studio-xci-bundle` Docker volume; containers run with
# your UID so generated files (_site/, Gemfile.lock) stay yours.

IMAGE  := ruby:3.3-bookworm
VOLUME := studio-xci-bundle
UID    := $(shell id -u)
GID    := $(shell id -g)
DOCKER := docker run --rm -v "$(CURDIR)":/site -v $(VOLUME):/usr/local/bundle -w /site \
          --user $(UID):$(GID) -e HOME=/tmp

.PHONY: install serve build clean

install:
	docker run --rm -v $(VOLUME):/usr/local/bundle $(IMAGE) chown -R $(UID):$(GID) /usr/local/bundle
	$(DOCKER) $(IMAGE) bundle install

serve: install
	$(DOCKER) -it -p 4000:4000 -p 35729:35729 $(IMAGE) \
		bundle exec jekyll serve --host 0.0.0.0 --livereload

build: install
	$(DOCKER) -e JEKYLL_ENV=production $(IMAGE) bundle exec jekyll build

clean:
	rm -rf _site .jekyll-cache .sass-cache
