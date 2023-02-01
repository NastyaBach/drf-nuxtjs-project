<template>
  <div class="container-fluid home-slider">
    <div id="carouselExampleCaptions" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleCaptions" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleCaptions" data-slide-to="1"></li>
        <li data-target="#carouselExampleCaptions" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="/img/first_img.jpg" class="d-block w-100" alt="Первая картинка">
          <div class="carousel-caption d-none d-md-block">
            <h5>Добро пожаловать в мой блог</h5>
            <p>Здесь вы можете прочесть статьи на самые разные темы</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="/img/second_img.jpg" class="d-block w-100" alt="Вторая картинка">
          <div class="carousel-caption d-none d-md-block">
            <h5>Нажимая на определённый тег</h5>
            <p>Вам будут показаны все статьи по данной теме</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="/img/third_img.jpg" class="d-block w-100" alt="Третья картинка">
          <div class="carousel-caption d-none d-md-block">
            <h5>После регистрациии</h5>
            <p>Вы сможете оставлять комментарии под постами</p>
          </div>
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleCaptions" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleCaptions" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "Slider"
}
</script>

<style scoped>

</style>