<template>
    <div class="section__hedline">
        <h1>{{ credential?.username }}@{{ credential?.app.name }}</h1>
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
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { CredentialSchema, Credential, AppType } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts';
import { getCredential, updateCredential, deleteCredential } from './components/credentialCRUD.ts';
import CredentialForm from './views/CredentialForm.vue';

const credentialId = document.querySelector('meta[name="credential-id"]')?.getAttribute('content');

export default defineComponent({
    components: {
        CredentialForm,
    },
    setup() {      
        const credential = ref<Credential>()
        const apps = ref<AppType[]>();
        
        async function getData(): Promise<void>{
            credential.value = await getCredential(credentialId?credentialId:"");
            apps.value = await getApps();
        }

        function saveCredential(credentialSchema: CredentialSchema){
            updateCredential(credentialId?credentialId:"", credentialSchema)
                .then((result: Credential) => {
                    credential.value = result;
                })
                .catch(error=>{
                    console.log(error);
                });
        }

        function destroyCredential(credentialSchema: CredentialSchema){
            deleteCredential(credentialId?credentialId:"", credentialSchema)
                .then((result: String) => {
                    window.location.href = "/dashboard";
                })
                .catch(error=>{
                    console.log(error);
                });
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