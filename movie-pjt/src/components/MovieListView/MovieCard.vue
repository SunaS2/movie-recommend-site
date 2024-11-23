<template>
  <div class="card-container">
    <div>
      <div class="movie-card">
        <img
          :src="store.getImgUrl(movie.poster_path, 200)"
          alt=""
          class="card-img"
        />
      </div>
      <div class="movie-container">
        <div class="movie-titles">
          <h4 class="title-with-heart">
            {{ movie.title_kr }}
            <button
              v-if="!store.isLikedMovie(movie.id)"
              @click="store.addToggleWishMovie(movie.id)"
              class="heart-button"
            >
              🤍
            </button>
            <button
              v-else
              @click="store.addToggleWishMovie(movie.id)"
              class="heart-button"
            >
              💖
            </button>
          </h4>
          <h5>{{ movie.title }}</h5>
        </div>
        <button @click="moveToDetail(movie.id)" class="detail-button">
          Detail
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card-container {
  width: 100%;
  max-width: 300px; /* 카드 최대 크기 설정 */
  margin: auto;
}

.movie-card {
  text-align: center;
}

.card-img {
  width: 100%; /* 카드 이미지가 카드 크기에 맞도록 */
  height: auto;
  border-radius: 10px;
}

.movie-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin: 10px;
}

.movie-titles {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  overflow: hidden; /* 텍스트 넘침 방지 */
  text-overflow: ellipsis; /* 텍스트가 넘칠 경우 '...' 처리 */
}

.title-with-heart {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  overflow: hidden; /* 텍스트 넘침 방지 */
  white-space: nowrap; /* 한 줄로 표시 */
  text-overflow: ellipsis;
  font-size: calc(0.8rem + 0.5vw); /* 반응형 폰트 크기 */
}

h5 {
  font-size: calc(0.7rem + 0.4vw); /* 반응형 폰트 크기 */
}

.heart-button {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  margin-left: 10px;
}

.detail-button {
  margin-top: 10px;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: calc(0.7rem + 0.4vw); /* 반응형 폰트 크기 */
}

.detail-button:hover {
  background-color: #0056b3;
}
</style>

<script setup>
defineProps({
  movie: Object,
});

import { useMovieStore } from "@/stores/movie";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

const store = useMovieStore();
const router = useRouter();
const { userProfile } = storeToRefs(store);

const moveToDetail = function (movieId) {
  router.push({ name: "movie-detail", params: { movieid: movieId } });
};

// const isLikedMovie = function (movieId) {
//   return userProfile.value.wish_movies?.some(movie => movie.id===movieId)
// }
</script>

<style scoped>
.movie-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  position: relative;
}

.movie-titles {
  display: flex;
  flex-direction: column;
  text-align: left;
  position: relative;
}

.title-with-heart {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
}

.heart-button {
  margin-left: auto; /* 오른쪽 끝으로 이동 */
  background: none;
  border: none;
  font-size: 1.2rem; /* 버튼 크기 조정 */
  cursor: pointer;
}

.detail-button {
  position: absolute;
  right: 0;
  bottom: 0;
  border-radius: 20px; /* 버튼 모서리를 둥글게 */
  padding: 5px 15px; /* 버튼 크기 조정 */
  background-color: #007bff; /* 버튼 배경색 */
  color: white; /* 텍스트 색상 */
  border: none; /* 기본 테두리 제거 */
  cursor: pointer;
}

.detail-button:hover {
  background-color: #0056b3; /* 호버 시 색상 변경 */
}
</style>
