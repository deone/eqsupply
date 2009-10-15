VERSION=0.1
NAME=eqsupply
TOPDIR=/home/zedd/rpmbuild

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
	@cp -r account/ quote_generator/ $(NAME)-$(VERSION)/
	@cp -r templates/ $(NAME)-$(VERSION)/
	@cp -r site_media/ $(NAME)-$(VERSION)/
	@cp authbackends.* helpers.* __init__.* manage.py settings* urls.* $(NAME)-$(VERSION)/
	@cp -r sql $(NAME)-$(VERSION)/
	@cp INSTALL MANIFEST.in Makefile README TODO $(NAME)-$(VERSION)/
	@cp install.sh install.conf eqsupply.spec $(NAME)-$(VERSION)/
	@tar -czvf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)/*
	@rm -rf $(NAME)-$(VERSION)
	@echo "All Done"

distclean: clean
	@rm -rf $(NAME)-$(VERSION)*

rpm: dist
	@rpmbuild -tb $(NAME)-$(VERSION).tar.gz
	@mv $(TOPDIR)/RPMS/i386/$(NAME)*.rpm .
