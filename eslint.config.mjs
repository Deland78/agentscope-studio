// @ts-check

import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

export default tseslint.config(
    {
        ignores: [
            'bin/**',
            '**/proto/**',
            'node_modules/**',
            'dist/**',
            'build/**',
            'coverage/**',
            '.next/**',
            '.nuxt/**',
            '.vuepress/dist/**',
            '.serverless/**',
            '.fusebox/**',
            '.dynamodb/**',
            '**/*.min.js',
            '**/*.min.css',
            '**/*.log',
            '**/*.lock',
            'package-lock.json',
            'yarn.lock',
            'pnpm-lock.yaml',
            '**/__pycache__/**',
            '**/*.pyc',
            '.git/**',
            '.vscode/**',
            '.idea/**',
        ],
    },
    eslint.configs.recommended,
    tseslint.configs.recommended,
);
