VERSION=0.1
NAME=eqsupply

all: build
	@echo "All Done"

build:
	@mkdir -p build/etc/httpd/conf.d
	@mkdir -p build/usr/local/www/eqsupply
	@mkdir -p build/var/lib/eqsupply/sql
	@mkdir -p build/usr/bin
	@cp -r account/ apache/ quote_generator/ site_media/ templates/ build/usr/local/www/eqsupply/
	@cp authbackends.* helpers.* __init__.* manage.py settings* urls.* build/usr/local/www/eqsupply/
	@cp conf/eqsupplymod_wsgi.conf build/etc/httpd/conf.d/
	@cp sql/* build/var/lib/eqsupply/sql/
	@cp bin/eqsupply-setup build/usr/bin/

install: build
	@./install.sh $(DESTDIR)

clean:
	@rm -rf build

dist: distclean
	@mkdir -p $(NAME)-$(VERSION)
	@cp -r bin $(NAME)-$(VERSION)/
	@cp -r conf $(NAME)-$(VERSION)/
	@cp -r apache $(NAME)-$(VERSION)/
	@cp -r account/ quote_generator/ site_media/ templates/ 
	@cp authbackends.* helpers.* __init__.* manage.py settings* urls.* $(NAME)-$(VERSION)/
	@cp -r sql $(NAME)-$(VERSION)/
	@cp INSTALL MANIFEST.in Makefile README TODO $(NAME)-$(VERSION)

distclean: clean
	@rm -rf $(NAME)-$(VERSION)*
