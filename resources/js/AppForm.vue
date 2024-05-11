<template>
    <div class="form__wrapper">
        <div class="form__field">
            <select name="apptype" v-model="selectedApptype">
                <option value="" disabled>Select type:</option>
                <option v-for="appType in appTypes" :value="appType.id">
                    {{ appType.name }}
                </option>
            </select>
        </div>
        <div class="form__field">
            <input v-model="selectedName" type="text" name="name" placeholder="Name">
        </div>
        <div class="form__buttons">
            <button :disabled="disableSubmit" type="submit" class="button">Save</button>
        </div>
    </div>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref, computed } from 'vue';
import { AppType } from './components/interfaces.ts';
import { getAppTypes } from './components/appTypeCRUD.ts';

export default defineComponent({
    setup() {
        const selectedName = ref<string>("");
        const selectedApptype = ref<string>("");
        const appTypes = ref<AppType[]>();
        const disableSubmit = computed(()=>{
            return selectedName.value == "" || selectedApptype.value == "";
        })
        
        async function getData(): Promise<void>{
            appTypes.value = await getAppTypes();
            console.log(appTypes.value);
        }

        onMounted(() => {
            getData(); 
        });

        return {
            selectedName,
            selectedApptype,
            appTypes,
            disableSubmit
        }
    }
});
</script>