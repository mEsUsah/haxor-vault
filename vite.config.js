import { defineConfig } from 'vite'
import { djangoVitePlugin } from 'django-vite-plugin'

export default defineConfig({
    server: { 
        hmr: {
            host: 'localhost',
        },
        watch: {
            usePolling: true
        }
    },
    build: {
        emptyOutDir: false,
    },
    plugins: [
        djangoVitePlugin({
            input: [
                'resources/scss/main.scss',
                'resources/js/main.js'
            ],
            pyPath: "python3",
            reloader: true,
            delay: 0
        })
    ],
});