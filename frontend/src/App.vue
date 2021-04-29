<template>
  <div id="app">
    <div class="content">
      <router-view/>
    </div>
    <footer>
      <p>Development team:</p>
      <div class="logo zip"></div>
      <div class="logo hdd"></div>
      <div class="logo idea"></div>
    </footer>
  </div>
</template>

<style lang="scss">

@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital@1&family=Poppins:ital,wght@0,300;0,400;0,900;1,900&display=swap');

body {
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.background {
  background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%), linear-gradient(to top, #000000 0%, #ffffff 100%);
}

.content {
  flex: 1 0 auto;
}

.side-flip-logo {
  display: flex;
  flex-direction: row;
  position: absolute;
  top: 0;
  margin-top: 22px;
}
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
    bottom: 5px;
    z-index: -1;
    width: 100%;
    height: 16px;
    background-color: #ffcc00;
  }
}
textarea,
select,
input {
  border: 4px solid #3098f3;
  background-color: #ffffff;
  line-height: 60px;
  font-family: Poppins;
  font-size: 20px;
  line-height: 48px;
  font-weight: 400;
}
label {
  color: #252525;
  font-family: "IBM Plex Mono";
  font-style: italic;
  font-size: 20px;
  line-height: 60px;
}
input[type=text] {
  padding-left: 10px;
  padding-right: 10px;
}
input[type=number] {
  width: 60px;
}

footer {
  // position: relative;
  width: 100%;
  flex-shrink: 0;
  // min-height: 100px;
  background: #ffffff;
  border-top: 1px solid #3098f3;
  // overflow: hidden;
  display: block;

  p {
    color: #252525;
    font-family: Poppins;
    font-size: 16px;
    font-weight: 300;
    line-height: 14px;
    padding: 10px;
    margin: 0;
    margin-top: -9px;
    line-height: 100px;
    float: left;
    @media (max-width: 575px) {
      display: none;
    }
  }
  .logo {
    width: 100px;
    height: 100px;
    float: left;
    // background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    &.zip {
      background-image: url('./assets/ZiP_logo.png');
    }
    &.hdd {
      background-image: url('./assets/HDD_logo.png');
      width: 180px;
    }
    &.idea {
      background-image: url('./assets/IDEA_logo.png');
    }
    &.eu {
      background-image: url('./assets/EU_logo.png');
      width: 240px;
      float: right;
    }
  }
}
.split-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: nowrap;
  .split {
    min-width: 320px;
    width: 100%;
    min-height: calc(100vh - 600px);
    flex: 1;
    padding: 80px;
    &.left {
      background-color: #f5f2e7;
      // background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%);
      background-image: linear-gradient(to right, #f5f0e2 0%, #fbfbfa 100%);
    }
  }
  @media (max-width: 1199px) {
    flex-wrap: wrap;
    .split {
      flex-shrink: 0;
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

  .split-right {
    padding: 0px;
    height: 100vh;
    min-width: 320px;
    width: 100%;
    flex: 1;
    overflow-y: auto;
    scrollbar-width: none; /* Firefox */
    -ms-overflow-style: none;  /* Internet Explorer 10+ */
  }
  .split-right::-webkit-scrollbar {display: none;}

.login-container {
  height: 100%;
  display: flex;
  justify-content: center;

  .wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
    padding: 10px;

    @media (min-width: 576px) {
      width: 75%
    }

    @media (min-width: 992px) {
      width: 50%
    }

    @media (min-width: 1400px) {
      width: 33%
    }

    .debate-logo {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin-top: 25px;

      @media (min-width: 768px) {
        flex-direction: row;
        margin-top: 50px;
      }

      img {
        width: 240px;
        margin-bottom: 20px;

        @media (min-width: 768px) {
          margin-bottom: 0;
          margin-right: 20px;
        }
      }

      span {
        color: #252525;
        font-family: Poppins;
        font-size: 18px;
        line-height: 29px;
        text-align: center;

        @media (min-width: 768px) {
          text-align: left;
        }
      }
    }

    .registration-form-container {
      display: flex;
      flex-direction: column;
      background-color: #ffffff;
      padding: 20px 20px 0 20px;
      margin-top: 40px;
      margin-bottom: 40px;

      @media (min-width: 768px) {
        padding: 40px 40px 0 40px;
        margin-top: 80px;
      }

      h1 {
        font-size: 24px;
        line-height: 32px;
        text-align: center;
        margin: 0;

        @media (min-width: 768px) {
          font-size: 30px;
          line-height: 40px;
          text-align: left;
          margin: 20px 0;
        }
      }

      label {
        line-height: 32px;
        font-size: 16px;
        display: block;
        margin-top: 10px;

        @media (min-width: 768px) {
          line-height: 40px;
          font-size: 20px;
        }
      }

      input {
        box-sizing: border-box;
        width: 100%;
      }
    }

    .link, .login-text {
      font-family: Poppins;
      font-size: 14px;
      line-height: 28px;
      color: #252525;

      @media (min-width: 768px) {
        font-size: 18px;
        line-height: 32px;
      }
    }

    .link {
      text-decoration: underline;

      &:hover {
        color: #3098f3;
      }
    }

    .line {
      margin-top: 26px;
      margin-bottom: 0;
      width: 100%;
    }

    .login-text {
      text-align: center;
    }

    .password-reset-text {
      text-align: right;
    }

    button {
      box-shadow: none;
      border: none;
      padding: 10px 20px;
      border-radius: 32px;
      background-color: #3098f3;
      opacity: 0.7;
      color: #ffffff;
      font-family: "Poppins";
      font-style: italic;
      font-size: 20px;
      text-transform: uppercase;
      letter-spacing: 2.16px;
      display: block;
      margin-top: 26px;
      cursor: pointer;
      float: right;

      @media (min-width: 768px) {
        font-size: 24px;
        padding: 12px 32px;
      }
    }

    button:disabled {
      opacity: 0.1;
    }

    button:hover {
      opacity: 1;
    }
  }
}

</style>
