<template>
  <div class="content-wrapper">
    <div class="content">
      <router-view/>
    </div>
    <footer>
      <div class="left-side">
        <p>Development team:</p>
        <img src="./assets/ZiP_logo.png" alt="ZiP logo">
        <img src="./assets/HDD_logo.png" alt="HDD logo">
        <img src="./assets/IDEA_logo.png" alt="IDEA logo">
      </div>
      <img src="./assets/EU_logo.png" alt="EU logo">
    </footer>
  </div>
</template>

<style lang="scss">
@import 'src/index.scss';

a:link {
    color: #252525;
}

h1 {
  color: #252525;
  font-family: "Poppins";
  font-size: 24px;
  font-weight: 900;
  line-height: 48px;
  position: relative;
  display: inline-block;
  &::before {
    content: '';
    display: block;
    position: absolute;
    bottom: 15px;
    z-index: -1;
    width: 100%;
    height: 16px;
    background-color: #ffcc00;
  }
}

footer {
  flex-shrink: 0;
  background: #ffffff;
  border-top: 1px solid #3098f3;
  padding: 8px 16px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  img {
    max-height: 40px;
    margin-right: 40px;
    margin-bottom: 10px;

    @media (min-width: 576px) {
      margin: 0;
    }

    @media (min-width: 992px) {
      margin-left: 40px;
      max-height: 60px;
    }
  }

  .left-side {
    margin: 10px 0;

    img {
      margin: 10px;

      @media (min-width: 576px) {
        margin: 0 20px 0 0;
      }

      @media (min-width: 768px) {
        margin-right: 20px;
      }

      @media (min-width: 992px) {
        margin-left: 40px;
        margin-right: 0;
      }
    }
  }

  @media (min-width: 576px) {
    padding: 15px 30px;
    justify-content: space-between;
    flex-direction: row;
  }

  p {
    color: #252525;
    font-family: Poppins;
    font-size: 16px;
    font-weight: 300;
    line-height: 60px;
    margin: 0;
    float: left;
    display: none;

    @media (min-width: 992px) {
      display: block;
    }
  }
}

@media (max-width: 1119px) {
  h1 {
    font-size: 22px;
  }
}
.modal {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(48, 152, 243, 0.8);
  z-index: 10;
}
.modal-inner {
  max-width: 500px;
  margin: auto;
  margin-top: 100px;
  background-color: #ffffff;
  padding: 100px;
}
@media (max-width: 767px) {
  .team-heading {
    width: calc(100% - 24px) !important;
  }
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) {
  .visible-xs {
    display: none !important;
  }
}

</style>
