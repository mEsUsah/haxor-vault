<template>
    <CredentialForm
        :newCredential="true"
        :apps="apps"
        @saveCredential="saveCredential"
    ></CredentialForm>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { CredentialSchema, Credential, App } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts';
import { createCredential } from './components/credentialCRUD.ts';
import CredentialForm from './views/CredentialForm.vue';

export default defineComponent({
    components: {
        CredentialForm,
    },
    setup() {      
        // View setup
        const apps = ref<App[]>();
        
        /**
         * Save credential.
         * 
         * Redirects to dashboard if successfull.
         * 
         * @param {CredentialSchema} credential 
         * @returns {void}
         */
        function saveCredential(credential: CredentialSchema){
            createCredential(credential)
                .then((result: Credential) => {
                    window.location.href = "/dashboard";
                })
                .catch(error=>{
                    console.log(error);
                });
        }

        /**
         * Get data needed by view.
         * 
         * @returns {Promise<void>}
         */
        async function getData(): Promise<void>{
            apps.value = await getApps();
        }

        onMounted(() => {
            getData(); 
        });

        return {
            apps,
            saveCredential,
        }
    }
});
</script>