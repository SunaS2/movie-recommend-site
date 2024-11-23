<template>
  <div class="movie-recommend-banner">
    <h4 class="banner-title">오늘 이런 영화 어떠세요?</h4>
    <div id="movieCarousel" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div
          v-for="(movie, index) in randomMovies"
          :key="movie.id"
          class="carousel-item"
          :class="{ active: index === 0 }"
        >
          <MovieRecommendBanerPosterCard :movie="movie" />
        </div>
      </div>
      <!-- 좌/우 컨트롤 버튼 -->
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#movieCarousel"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#movieCarousel"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import MovieRecommendBanerPosterCard from "./MovieRecommendBanerPosterCard.vue";
const props = defineProps({
  randomMovies: Array,
});
</script>

<style scoped>
.carousel {
  position: relative;
  width: 100%;
}

.carousel-inner {
  display: flex;
  flex-wrap: nowrap; /* 카드가 줄 바꿈되지 않도록 설정 */
  overflow-x: hidden; /* 넘치는 부분은 숨기기 */
}

.carousel-item {
 /* 한 번에 3개의 카드가 보이도록 설정 */
  padding: 10px;
  transition: transform 0.5s ease-in-out;
  box-sizing: border-box; /* 패딩 포함한 크기 계산 */
}

@media (max-width: 768px) {
  .carousel-item {
    flex: 0 0 50%; /* 작은 화면에서는 2개씩 표시 */
  }
}

@media (max-width: 576px) {
  .carousel-item {
    flex: 0 0 100%; /* 더 작은 화면에서는 1개씩 표시 */
  }
}

.movie-card {
  width: 200px;
  margin: 0 auto;
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 10px;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
  background-color: rgba(0, 0, 0, 0.5); /* 버튼 배경 반투명 */
  border-radius: 50%; /* 원형 버튼 */
  padding: 10px;
}
</style>
