<template>
    <div v-if="vocaList && !isDeleted" id="voca-note">
        <div v-if="userProfile.username === store.logedinUsername">
            <div class="button-container">
                <button v-if="userProfile.username === store.logedinUsername" @click="deleteNote(vocaList.movies[0].id)"
                    class="voca-button">
                    <font-awesome-icon :icon="['fas', 'trash-can']" />
                </button>
                <div>
                    <button v-if="vocaList.is_public" @click="togglePublic(vocaList.movies[0].id)" class="voca-button">
                        <font-awesome-icon :icon="['fas', 'lock-open']" class="locker-icon" />
                    </button>
                    <button v-else @click="togglePublic(vocaList.movies[0].id)" class="voca-button">
                        <font-awesome-icon :icon="['fas', 'lock']" class="locker-icon" />
                    </button>
                </div>
            </div>
        </div>
        <h1 class="voca-title">{{ vocaList.movies[0].title }}'s vocanote</h1>
        <VocaCreate :note="vocaList" />
        <button @click="toggleDeleteButtons">{{ showDeleteButton ? '취소' : '삭제' }}</button>
        <button @click="toggleUpdateButtons">{{ showUpdateButton ? '취소' : '수정' }}</button>
        <VocaListRead v-for="voca in vocaList.vocas" :key="voca.id" :voca="voca" :show-delete="showDeleteButton"
            :show-update="showUpdateButton" @delete-event="deleteWord" @update-event="updateWord"
            @check-event="toggleMemorized" />
    </div>
    <div v-if="isDeleted" class="deleted-message">
        <p>삭제 되었습니다.</p>
        <button @click="returnToMyNote()">내 Voca Note List 보러가기</button>
    </div>
</template>



<script setup>
import { useMovieStore } from "@/stores/movie";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import VocaCreate from "@/components/VocaNotePopUpView/VocaCreate.vue";
import VocaListRead from "@/components/VocaNotePopUpView/VocaListRead.vue";
import { storeToRefs } from "pinia";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const store = useMovieStore()
const route = useRoute()

// const note = ref(null)
const showDeleteButton = ref(false)
const showUpdateButton = ref(false)
const { userProfile, vocaList } = storeToRefs(store)
const noteId = ref(null)

const emit = defineEmits(['deleteEvent', 'toggleEvent'])
const isDeleted = ref(false)

const deleteNote = function (movieId, userId = userProfile.value.id) {
    const result = window.confirm('Really????')
    if (result) {
        store.deleteNote(movieId, userId)
        isDeleted.value = true
    } else {
        return null
    }
}

const returnToMyNote = function (username = userProfile.value.username) {
    if (window.opener) {
        window.opener.location.reload(); // 부모 창 새로고침
    }
    window.close()

}

const togglePublic = function (movieId, userId = userProfile.value.id) {
    store.togglePublicVocaNote(movieId, userId)
    if (window.opener) {
        window.opener.location.reload(); // 부모 창 새로고침
    }
    // emit('toggleEvent', movieId, userId)
}

const deleteWord = function (id) {
    store.deleteVoca(id, noteId.value)
}

const updateWord = function (id, payload) {
    // axios put
    store.updateVoca(id, noteId.value, payload)
}

const toggleMemorized = function (id) {
    // axios post
    store.memorizedVoca(id, noteId.value)
}

const toggleDeleteButtons = function () {
    showDeleteButton.value = !showDeleteButton.value
}

const toggleUpdateButtons = function () {
    showUpdateButton.value = !showUpdateButton.value
}

onMounted(() => {
    noteId.value = route.params.note_id
    store.getVocas(noteId.value)
    isDeleted.value = false
})

</script>

<style scoped>
/* #voca-note {
    font-family: 'Arial', sans-serif;
    padding: 20px;
    background-color: #f9f9f9;
} */

.button-container {
    display: flex;
    justify-content: space-between;
    /* 버튼을 양쪽으로 정렬 */
    align-items: center;
    width: 100%;
    /* 필요한 경우 너비 조정 */
    gap: 10px;
    /* 버튼 사이의 간격 */
}


.voca-button {
    background-color: transparent;
    border: none;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 14px 20px;
    /* 세로를 더 통통하게 */
    font-size: 14px;
    font-weight: 750;
    color: #434040;
    background: rgba(255, 255, 255, 0.15);
    /* 살짝 투명한 배경 */
    backdrop-filter: blur(8px);
    /* 유리효과 */
    border-radius: 20px;
    /* 둥근 모서리 */
    border: 1px solid rgba(90, 90, 90, 0.226);
    /* 연한 테두리 */
    cursor: pointer;
    gap: 8px;
    /* 아이콘과 텍스트 간격 */
    transition: background 0.3s ease, transform 0.2s ease;
    /* 부드러운 효과 */
    text-decoration: none;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
.voca-title {
  font-size: 1.8rem;
  font-weight: bold;
  color: #fff;
  margin: 1rem;
}
</style>
