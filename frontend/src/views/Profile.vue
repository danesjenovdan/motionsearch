<template>
<div class="background container">
  <div class="header">
    <div class="logo">
      <router-link to="/"><img src="../assets/motion-generator-logo.svg" alt="motion generator logo"></router-link>
      <span>Easiest way to find a motion for debating</span>
    </div>
    <div class="header-buttons">
      <router-link to="/motionSuggest" class="button button--suggest"><span>Suggest a motion </span></router-link>
      <router-link to="/login" v-if="!isAuth" class="button button--pan"><span>Log in</span></router-link>
      <router-link to="/profile" v-if="isAuth" class="button button--pan"><span>Profile</span></router-link>
    </div>
  </div>
  <div class="wrapper">
    <div class="motionSuggestContainer">
        <div class='user-container'>
          <h1>{{username}}</h1>
          <p @click="reset">Change your password</p>
          <div/>
          <p @click="logout">Log out</p>
          <div/>
        </div>
        <motion-list type="getMyMotions" :headers="false" title="My submitted motions"/>
        <router-link to="/motionSuggest" class="button button--suggest suggest"><span>Suggest a motion </span></router-link>
        <motion-list type="getFavoritesMotions" :headers="false" title="Favourited Motions" />
    </div>
  </div>
</div>
</template>

<script>
import MotionList from '../components/MotionList.vue'


  export default {
    data() {
      return {
        username: '',
        isAuth: '',
      }
    },
    components: {
      MotionList,
    },
    methods : {
      reset() {
       this.$router.push('reset')
      },
      async logout() {
        await this.$store.dispatch('logout')
        this.$router.push('/login')
      }
    },
    async created() {
      this.isAuth = await this.$store.dispatch('isAuth')
      const user = await this.$store.dispatch('getMe')
      this.username = user[0].username
    }
  }
</script>


<style scoped lang="scss">

.container {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;

  .header {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #3098f3;
    padding-right: 30px;

    .logo {
      display: flex;
      align-items: center;

      span {
        font-family: Poppins;
        font-size: 18px;
        line-height: 29px;
        color: #252525;
        display: none;

        @media (min-width: 992px) {
          display: block;
        }
      }

      img {
        height: 30px;
        margin: 10px 10px 10px 30px;

        @media (min-width: 768px) {
          height: 40px;
          margin: 10px 10px 10px 40px;
        }

        @media (min-width: 768px) {
          height: 74px;
        }

        @media (min-width: 1200px) {
          margin: 10px 10px 10px 100px;
        }
      }
    }

    .button {
      @media (max-width: 575px) {
        padding: 5px 5px;
        font-size: 10px;
      }
    }
  }

  .wrapper {
    width: 100%;
    max-width: 900px;

    @media (min-width: 768px) {
      width: 75%
    }

    @media (min-width: 1200px) {
      width: 75%
    }

    .motionSuggestContainer {
      display: flex;
      flex-direction: column;
      background-color: #ffffff;
      padding: 10px 20px;
      margin: 40px 10px;

      @media (min-width: 768px) {
        margin: 60px 10px 40px;
        padding: 20px 40px;
      }

      button[type="submit"] {
        margin-bottom: 20px;
      }
    }
  }
}

.textAreaContainer {
  position: relative;
  margin-bottom: 30px;

  textarea {
    display: block;
    resize: none;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
  }
}

.user-container {
  padding: 0 20px;
  margin-bottom: 30px;

  @media (min-width: 992px) {
    padding: 0 40px;
  }

  p {
    color: #252525;
    font-family: Poppins;
    font-size: 20px;
    @media (min-width: 992px) {
      font-size: 24px;
    }

  }
  p:hover {
    cursor: pointer;
  }
  h1 {
    color: #252525;
    font-family: "Poppins";
    font-size: 20px;
    margin-bottom: 0;
    font-weight: bold;

    @media (min-width: 992px) {
      font-size: 30px;
    }
  }
  div {
    margin: 0;
    border-top: 1px solid black;
    width: 100%
  }
}

.inputContainer {
  display: flex;
  border-top: 1px solid black;
  padding: 10px;
  flex-direction: column;

  @media (min-width: 576px) {
    flex-direction: row;
    justify-content: space-between;
  }

  & > label {
    @media (min-width: 576px) {
      line-height: 60px; //  must be same as input height
    }
  }

  .select-wrapper, .select-wrapper-full {
    width: 100%;
    cursor: pointer;
    position: relative;

    @media (min-width: 576px) {
      width: 50%;
    }

    select {
      width: 100%;
      -moz-appearance: none;
      -webkit-appearance: none;
      appearance: none;
      padding-right: 50px;
      cursor: pointer;
    }

    &:after {
      content: "";
      width: 25px;
      height: 25px;
      top: 10px;
      right: 10px;
      background-image: url("../assets/dropdown.svg");
      background-size: contain;
      position: absolute;

      @media (min-width: 768px) {
        width: 30px;
        height: 30px;
        top: 15px;
        right: 15px;
      }
    }
  }

  .arrayContainer {
    display: flex;
    flex-direction: column;
    @media (min-width: 576px) {
      width: 50%;
    }

        .select-wrapper-full {
          width: 100%;
          @media (min-width: 576px) {
            width: 100%;
          }
        }



    span {
      padding: 14px 28px 14px 0;
      font-size: 16px;
      display: inline-block;
      cursor: pointer;
    }

    input {
      margin-bottom: 10px;
      width: 100%
    }

  }

  &:last-child {
    align-items: start;
  }

  .buttonContainer {
    display: flex;
    justify-content: flex-end;
    align-items: center;

    p {
      font-family: "IBM Plex Mono";
    }

    .addLink {
      background-image: url("../assets/plus.png");
      background-repeat: no-repeat;
      background-position: center;
      width: 42px;
      height: 42px;
      // border-radius: 21px;
      // background-color: #3098f3;
    }
  }
}

.radioContainer {
  display: flex;
  justify-content: space-evenly;
  width: 50%;
}

.subtitle {
  color: #252525;
  font-family: "IBM Plex Mono";
  font-size: 12px;
  font-style: italic;
  display: block;
  margin-top: -5px;

  @media (min-width: 768px) {
    font-size: 14px;
    line-height: 16px;
  }
}

.line {
  margin-top: 26px;
  border-top: 1px solid;
}

.setting-container {
  width: 50%;

  @media (min-width: 768px) {
    display: flex;
    justify-content: start;

  }

  .radio-container {
    padding-left: 2px;
    font-family: Poppins;
    font-size: 16px;
    line-height: 48px;
    display: block;
    float: left;
    overflow: hidden;
    @media (min-width: 768px) {
      font-size: 20px;
      line-height: 60px;
    }
    span {
      display: block;
      float: right;
      padding-left: 10px;
      width: auto;
    }
    &:nth-child(1) {
      margin-right: 20%;
      @media (min-width: 768px) {
        margin-right: 20%;
      }
    }
    input[type="radio"] {
      width: 30px;
      line-height: 60px;
      display: inline-block;
      top: 12px;
      @media (min-width: 768px) {
        top: 17px;
      }
    }
  }

  @supports(-webkit-appearance: none) or (-moz-appearance: none) {
    input[type='radio'] {
      --active: #ffffff;
      --active-inner: #3098f3;
      --focus: 2px rgba(39, 94, 254, .3);
      --border: #3098f3;
      --border-hover: #3098f3;
      --background: #fff;
      --disabled: #F6F8FF;
      --disabled-inner: #E1E6F9;
      -webkit-appearance: none;
      -moz-appearance: none;
      height: 25px;
      outline: none;
      display: inline-block;
      vertical-align: top;
      position: relative;
      margin: 0;
      cursor: pointer;
      // border: 4px solid var(--bc, var(--border));
      border: 3px solid #3098f3;
      border-radius: 50%;
      background: var(--b, var(--background));
      transition: background .3s, border-color .3s, box-shadow .2s;
      &:after {
        content: '';
        display: block;
        left: 0;
        top: 0;
        position: absolute;
        transition: transform var(--d-t, .3s) var(--d-t-e, ease), opacity var(--d-o, .2s);
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: var(--active-inner);
        opacity: 0;
        transform: scale(var(--s, .7));
      }
      &:checked {
        --b: var(--active);
        --bc: var(--active);
        --d-o: .3s;
        --d-t: .6s;
        --d-t-e: cubic-bezier(.2, .85, .32, 1.2);
      }
      &:disabled {
        --b: var(--disabled);
        cursor: not-allowed;
        opacity: .9;
        &:checked {
          // --b: var(--disabled-inner);
          // --bc: var(--border);
        }
        &+label {
          cursor: not-allowed;
        }
      }
      &:hover {
        &:not(:checked) {
          &:not(:disabled) {
            --bc: var(--border-hover);
          }
        }
      }
      &:focus {
        box-shadow: 0 0 0 var(--focus);
      }
      &:not(.switch) {
        width: 25px;
        &:after {
          opacity: var(--o, 0);
        }
        &:checked {
          --o: 1;
        }
      }
      &+label {
        font-size: 14px;
        line-height: 25px;
        display: inline-block;
        vertical-align: top;
        cursor: pointer;
        margin-left: 4px;
      }
    }

    input[type='checkbox'] {
      &:not(.switch) {
        border-radius: 7px;
        &:after {
          width: 5px;
          height: 9px;
          border: 2px solid var(--active-inner);
          border-top: 0;
          border-left: 0;
          left: 7px;
          top: 4px;
          transform: rotate(var(--r, 20deg));
        }
        &:checked {
          --r: 43deg;
        }
      }
      &.switch {
        width: 38px;
        border-radius: 11px;
        &:after {
          left: 2px;
          top: 2px;
          border-radius: 50%;
          width: 15px;
          height: 15px;
          background: var(--ab, var(--border));
          transform: translateX(var(--x, 0));
        }
        &:checked {
          --ab: var(--active-inner);
          --x: 17px;
        }
        &:disabled {
          &:not(:checked) {
            &:after {
              opacity: .6;
            }
          }
        }
      }
    }
  }
}

</style>
