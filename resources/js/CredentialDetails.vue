<template>
    <CredentialForm
        :newCredential="true"
        :credential="credential"
        :apps="apps"
        @saveCredential="saveCredential"
    ></CredentialForm>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, reactive, computed } from 'vue';
import { CredentialSchema, Credential, AppType } from './components/interfaces.ts';
import { getApps } from './components/appCRUD.ts';
import { getCredential } from './components/credentialCRUD.ts';
import CredentialForm from './views/CredentialForm.vue';

export default defineComponent({
    components: {
        CredentialForm,
    },
    setup() {      
        const credential = ref<Credential>()
        const apps = ref<AppType[]>();
        
        async function getData(): Promise<void>{
            credential.value = await getCredential(credentialId);
            console.log(credential.value);
            apps.value = await getApps();
        }

        function saveCredential(credential: CredentialSchema){
            // createCredential(credential)
            //     .then((result: Credential) => {
            //         console.log(result);
            //         window.location.href = "/credential/" + result.id;
            //     })
            //     .catch(error=>{
            //         console.log(error);
            //     });
        }

        onMounted(() => {
            getData(); 
        });

        return {
            apps,
            credential,
            saveCredential,
        }
    }
});
</script>