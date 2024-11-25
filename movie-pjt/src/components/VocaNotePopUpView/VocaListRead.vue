<template>
  <div id="voca">
    <input type="checkbox" id="is_memorized" @input="memorizedWord(voca.id)" v-model="voca.is_memorized">
      <span @click="toggleMemoShow">
        <span>{{ voca.word }}</span> : 
        <span>{{ voca.word_mean }}</span>
      </span>
    <button @click="deleteWord(voca.id)" v-if="showDelete" class="emoji-button"><font-awesome-icon :icon="['fas', 'trash-can']" /></button>
    <button @click="toggleFormShow" v-if="showUpdate" ><font-awesome-icon :icon="['fal', 'pen-to-square']" /></button>
    <br>
    <form v-if="isVisiable" @submit.prevent="updateWord(voca.id)" class="voca-form-container">
      <label for="word">word:</label>
      <input type="text" id="word" v-model.trim="word">
      <br>
      <label for="word_mean">mean:</label>
      <input type="text" id="word_mean" v-model.trim="word_mean">
      <br>
      <label for="examples">examples:</label>
      <input type="text" id="examples" v-model.trim="examples">
      <br>
      <label for="memo">memo:</label>
      <textarea id="memo" v-model.trim="memo"></textarea>
      <br>
      <input type="submit" id="submit" value="update">
    </form>
    <div v-if="isMemoVisiable">
      <p>예문: {{ voca.examples }}</p>
      <p>메모: {{ voca.memo }}</p>
    </div>
  </div>
</template>



<script setup>
import { ref } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const props = defineProps({
  voca:Object,
  showDelete:Boolean,
  showUpdate:Boolean
})
const emit = defineEmits(['deleteEvent', 'updateEvent', 'checkEvent'])
const isVisiable = ref(false)
const isMemoVisiable = ref(false)

const word = ref(props.voca.word)
const word_mean = ref(props.voca.word_mean)
const examples = ref(props.voca.examples)
const memo = ref(props.voca.memo)

const deleteWord = function (id) {
  emit('deleteEvent', id)
}

const updateWord = function (id) {
  const payload = {
    word: word.value,
    word_mean: word_mean.value,
    examples: examples.value,
    memo: memo.value
  }
  emit('updateEvent', id, payload)
}

const memorizedWord = function (id) {
  emit('checkEvent', id)
}

const toggleFormShow = function () {
  isVisiable.value = !isVisiable.value
}

const toggleMemoShow = function () {
  isMemoVisiable.value = !isMemoVisiable.value
}
</script>

<style scoped>
 .voca-form-container {
    background: rgba(255, 255, 255, 0.2); /* 반투명한 배경 */
    border: 1px solid rgba(255, 255, 255, 0.3); /* 테두리 */
    border-radius: 12px; /* 둥근 모서리 */
    padding: 16px; /* 내부 여백 */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 그림자 */
    backdrop-filter: blur(10px); /* 블러 효과 */
    max-width: 400px; /* 최대 너비 */
    margin: 16px auto; /* 가운데 정렬 */
  }

  .voca-form-container label {
    display: block; /* 라벨 블록 */
    margin-bottom: 8px; /* 아래 여백 */
    font-weight: bold; /* 두꺼운 글씨 */
    color: #fff; /* 흰색 글씨 */
  }

  .voca-form-container input[type="text"],
  .voca-form-container textarea {
    width: 100%; /* 입력창 너비 100% */
    padding: 8px; /* 내부 여백 */
    margin-bottom: 12px; /* 아래 여백 */
    border: 1px solid rgba(255, 255, 255, 0.4); /* 테두리 */
    border-radius: 8px; /* 둥근 입력창 */
    background: rgba(255, 255, 255, 0.2); /* 입력창 반투명 */
    color: #fff; /* 흰색 글씨 */
    font-size: 16px; /* 글씨 크기 */
  }

  .voca-form-container input[type="text"]:focus,
  .voca-form-container textarea:focus {
    outline: none; /* 포커스 시 기본 테두리 제거 */
    border: 1px solid rgba(255, 255, 255, 0.7); /* 포커스 테두리 색상 */
  }

  .voca-form-container input[type="submit"] {
    background: rgba(0, 123, 255, 0.8); /* 버튼 배경 */
    color: #fff; /* 흰색 글씨 */
    padding: 10px 16px; /* 버튼 여백 */
    border: none; /* 테두리 제거 */
    border-radius: 8px; /* 둥근 버튼 */
    font-size: 16px; /* 글씨 크기 */
    cursor: pointer; /* 포인터 커서 */
    transition: background 0.3s; /* 배경색 변화 */
  }

  .voca-form-container input[type="submit"]:hover {
    background: rgba(0, 123, 255, 1); /* 호버 배경색 */
  }

</style>