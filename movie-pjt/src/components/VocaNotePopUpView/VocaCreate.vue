<template>
  <div class="form-container">
    <form @submit.prevent="submitVoca(note.id)" class="voca-form">
      <div class="form-row">
        <label for="word">Word:</label>
        <input type="text" id="word" v-model.trim="word" class="form-input">
      </div>
      <div class="form-row">
        <label for="word_mean">Meaning:</label>
        <input type="text" id="word_mean" v-model.trim="word_mean" class="form-input">
      </div>
      <div class="form-row">
        <label for="examples">Examples:</label>
        <input type="text" id="examples" v-model.trim="examples" class="form-input">
      </div>
      <div class="form-row">
        <label for="memo">Memo:</label>
        <textarea id="memo" v-model.trim="memo" class="form-textarea"></textarea>
      </div>
      <div class="form-row submit-row">
        <input type="submit" id="submit" value="Update" class="submit-button">
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()

const word = ref(null)
const word_mean = ref(null)
const examples = ref(null)
const memo = ref(null)

defineProps({
  note:Object
})

const submitVoca = function (noteId = note.id) {
  //axios data 넘겨주기
  const payload = {
    word: word.value,
    word_mean: word_mean.value,
    examples: examples.value,
    memo: memo.value
  }

  store.createVoca(noteId, payload)
  
  word.value=""
  word_mean.value=""
  examples.value=""
  memo.value=""
}
</script>

<style scoped>
.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 40vh;
  background-color: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.voca-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-row {
  display: flex;
  align-items: center;
  gap: 16px;
}

label {
  font-size: 1rem;
  font-weight: bold;
  color: #333;
  width: 30%; /* 라벨 크기 */
  font-family: "Comic Sans MS", "Arial", sans-serif; /* 귀엽고 통통한 글씨체 */
}

.form-input,
.form-textarea {
  flex: 1;
  padding: 10px 14px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s ease;
}

.form-input:focus,
.form-textarea:focus {
  border-color: #007aff; /* Apple 스타일 블루 */
  box-shadow: 0 0 4px rgba(0, 122, 255, 0.5);
}

.form-textarea {
  resize: vertical;
  min-height: 80px;
}

.submit-button {
  background-color: #007aff;
  color: white;
  padding: 10px 14px;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 100%;
}

.submit-button:hover {
  background-color: #005bb5;
}

.submit-row {
  justify-content: flex-end;
  display: flex;
}
</style>