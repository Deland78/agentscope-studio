#!/usr/bin/env node

if (!process.env.NODE_ENV) {
    process.env.NODE_ENV = 'production';
}

require('../dist/server/src/index.js');
