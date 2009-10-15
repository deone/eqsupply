#!/bin/bash

. ./install.conf
DESTDIR=$1

install -d -m 755 ${DESTDIR}/$WWW_DIR/eqsupply
install -d -m 755 ${DESTDIR}/$CONFD_DIR
