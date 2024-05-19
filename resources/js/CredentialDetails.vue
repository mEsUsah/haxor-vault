<template>
    <div class="section__hedline">
        <div class="section__hedline-text">
            <h1>{{ credential?.app.name }}</h1>
            <p>{{ credential?.username }}</p>
        </div>
    </div>
    <hr>
    <CredentialForm
        :newCredential="false"
        :credential="credential"
        :apps="apps"
        @saveCredential="saveCredential"
        @destroyCredential="destroyCredential"
    ></CredentialForm>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import { CredentialSchema, Credential, App } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts';
import { getCredential, updateCredential, deleteCredential } from './components/credentialCRUD.ts';
import CredentialForm from './views/CredentialForm.vue';

const credentialId = document.querySelector('meta[name="credential-id"]')?.getAttribute('content');

export default defineComponent({
    components: {
        CredentialForm,
    },
    setup() {      
        // View setup
        const credential = ref<Credential>();
        const apps = ref<App[]>();
        
        /**
         * Save changes to credential.
         * 
         * @param {CredentialSchema} credentialSchema 
         * @returns {void}
         */
        function saveCredential(credentialSchema: CredentialSchema): void{
            updateCredential(credentialId?credentialId:"", credentialSchema)
                .then((result: Credential) => {
                    credential.value = result;
                })
                .catch(error=>{
                    console.log(error);
                });
        }

        /**
         * Delete credential.
         * 
         * @param {CredentialSchema} credentialSchema 
         * @returns {void}
         */
        function destroyCredential(credentialSchema: CredentialSchema): void{
            deleteCredential(credentialId?credentialId:"", credentialSchema)
                .then((result: String) => {
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
            credential.value = await getCredential(credentialId?credentialId:"");
            apps.value = await getApps();
        }

        onMounted(() => {
            getData(); 
        });

        return {
            apps,
            credential,
            saveCredential,
            destroyCredential,
        }
    }
});
</script>