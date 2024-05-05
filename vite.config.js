import { defineConfig } from 'vite'
import vue from "@vitejs/plugin-vue";
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
        vue(),
        djangoVitePlugin({
            input: [
                'resources/scss/main.scss',
                'resources/js/main.ts',
                'resources/js/login.ts'
            ],
            pyPath: "python3",
            reloader: true,
            delay: 0
        })
    ],
});