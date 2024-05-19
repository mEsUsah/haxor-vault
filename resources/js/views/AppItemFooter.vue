<template>
    <div class="app-item__footer">
        <a :href="getCreateCredentialUrl(app)" class="button button--danger">&plus; Add credential</a>
    </div>
</template>
<script lang="ts">
import { defineComponent, PropType} from 'vue';
import { App } from '../components/interfaces.ts';

export default defineComponent({
    props: {
        app: {
            type: Object as PropType<App>,
            required: false
        }
    },
    setup() {
        /**
         * Get create credential URL.
         * 
         * Includes current app-id as a query parameter.
         * 
         * Used when navigating to create credential page.
         * @param app 
         */
        function getCreateCredentialUrl(app: App){
            return "/credential/create?app=" + app?.id;
        }

        return {
            getCreateCredentialUrl
        }
    }
});
</script>