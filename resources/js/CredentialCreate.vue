<template>
    <CredentialForm
        :newCredential="true"
        :apps="apps"
        @saveCredential="saveCredential"
    ></CredentialForm>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { CredentialSchema, Credential, AppType } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts';
import { createCredential } from './components/credentialCRUD.ts';
import CredentialForm from './views/CredentialForm.vue';

export default defineComponent({
    components: {
        CredentialForm,
    },
    setup() {      
        const apps = ref<AppType[]>();
        
        async function getData(): Promise<void>{
            apps.value = await getApps();
        }

        function saveCredential(credential: CredentialSchema){
            createCredential(credential)
                .then((result: Credential) => {
                    window.location.href = "/credential/" + result.id;
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
            saveCredential,
        }
    }
});
</script>