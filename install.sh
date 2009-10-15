#!/bin/bash

. ./install.conf
DESTDIR=$1

install -d -m 755 ${DESTDIR}/$WWW_DIR/eqsupply
install -d -m 755 ${DESTDIR}/$CONFD_DIR
install -d -m 755 ${DESTDIR}/var/lib/eqsupply
install -d -m 755 ${DESTDIR}/usr/bin

install -m 644 build/etc/httpd/conf.d/eqsupplymod_wsgi.conf ${DESTDIR}/$CONFD_DIR/eqsupplymod_wsgi.conf

install -m 755 build/usr/bin/eqsupply-setup ${DESTDIR}/usr/bin/eqsupply-setup

cp -r build/usr/local/www/eqsupply ${DESTDIR}/usr/local/www/
cp -r build/var/lib/eqsupply/* ${DESTDIR}/var/lib/eqsupply
