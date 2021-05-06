<template>
<div class="background container">
  <div class="header">
    <div class="logo">
      <img src="../assets/motion-generator-logo.svg" alt="motion generator logo">
      <span>Easiest way to find a motion for debating</span>
    </div>
    <div class="header-buttons">
      <router-link to="/motionSuggest" class="btn">Suggest a motion</router-link>
      <router-link to="/login" class="btn login">Log in</router-link>
    </div>
  </div>
  <div class="wrapper">
    <div class="motionSuggestContainer">
      <h1>Suggest a motion</h1>
      <form>
        <div class="textAreaContainer">
          <label>Motion text</label>
          <textarea rows="3" cols="20" name="text"></textarea>
         </div>
        <div class="inputContainer">
          <label>Topic</label>
          <select name="Topic" id="topic">
            <option value=null>Select</option>
            <option value="volvo">Volvo</option>
            <option value="saab">Saab</option>
            <option value="opel">Opel</option>
            <option value="audi">Audi</option>
          </select>
        </div>
        <div class="inputContainer">
          <label>Difficulty</label>
          <select name="Difficulty" id="difficulty">
            <option value=null>Select</option>
            <option value="volvo">Volvo</option>
            <option value="saab">Saab</option>
            <option value="opel">Opel</option>
            <option value="audi">Audi</option>
          </select>
        </div>
        <div class="inputContainer">
          <label>Age</label>
          <select name="Age" id="age">
            <option value=null>Select</option>
            <option value="volvo">Volvo</option>
            <option value="saab">Saab</option>
            <option value="opel">Opel</option>
            <option value="audi">Audi</option>
          </select>
        </div>
        <div class="inputContainer">
          <label>Motion type</label>
          <select name="motionType" id="motionType">
            <option value=null>Select</option>
            <option value="volvo">Volvo</option>
            <option value="saab">Saab</option>
            <option value="opel">Opel</option>
            <option value="audi">Audi</option>
          </select>
        </div>
        <div class="inputContainer">
          <label>Training focus</label>
          <select name="trainingFocus" id="trainingFocus">
            <option value=null>Select</option>
            <option value="volvo">Volvo</option>
            <option value="saab">Saab</option>
            <option value="opel">Opel</option>
            <option value="audi">Audi</option>
          </select>
        </div>
        <div class="inputContainer">
          <label>Impro or prep</label>
        <div class="setting-container">
          <div class="radio-container">
            <span class="label">impro</span>
            <input
              type="radio"
              name="impro/prep"
              :value="impro"
              >
          </div>
          <div class="radio-container">
            <span class="label">prep</span>
            <input
              type="radio"
              name="impro/prep"
              :value="prep"
              >
          </div>
        </div>
        </div>
        <div class="inputContainer">
          <div class="subtitleContainer">
            <label>Add is used where</label>
            <span class="subtitle">Press ENTER after each input</span>
          </div>
          <div class="arrayContainer">
            <div v-for="(element, index) in usedWhere" :element="element" :key="element" :vid-id="index">
              <p><button v-on:click="removeUsedWhere(index)" class="btn">x</button> {{element}}</p>
            </div>
            <input type="text" key="used" placeholder="Type here..." @keydown.enter="addUsedWhere"/>
          </div>
        </div>
        <div class="inputContainer">
          <div class="subtitleContainer">
            <label>Add links</label>
            <span class="subtitle">Press ENTER after each input</span>
          </div>
          <div class="arrayContainer">
            <div v-for="(link, index) in links" :link="link" :key="link" :vid-id="index">
               <div><span v-on:click="removeLink(index)" class="">x</span> <a target="_blank" :href="link.url">{{link.title}}</a></div>
            </div>
            <input type="text" key="link.title" placeholder="Type here..." />
            <input type="text" key="link.url" placeholder="Type here..." />
          </div>
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<script>
const usedWhere = []
const links = [{
  title: "yeet",
  url:"www.yeet.com"
}]

export default {
  data() {
    return {
      usedWhere,
      links
    }
  },
  methods: {
    addUsedWhere: (event) => {
      event.preventDefault()
      usedWhere.push(event.target.value)
    },
    removeUsedWhere: (index) => {
      event.preventDefault()
      usedWhere.splice(index, 1)
      console.log('usedWhere: ', usedWhere);
    }
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
        height: 50px;
        margin: 10px 10px 10px 30px;
        display: none;

        @media (min-width: 768px) {
          display: block;
        }

        @media (min-width: 768px) {
          height: 80px;
        }

        @media (min-width: 1200px) {
          margin: 10px 10px 10px 100px;
        }
      }
    }

    .header-buttons {
      margin: 20px 30px 20px 0;

      @media (min-width: 1200px) {
        margin-right: 60px;
      }
    }
  }

  .wrapper {
    width: 100%;

    @media (min-width: 768px) {
      width: 75%
    }

    @media (min-width: 1200px) {
      width: 50%
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

.inputContainer {
  display: flex;
  border-top: 1px solid black;
  padding: 10px;
  justify-content: space-between;
  align-items: center;

  .arrayContainer {
    display: flex;
    flex-direction: column;
    width: 50%;

    span {
      padding: 14px 28px 14px 0;
      font-size: 16px;
      display: inline-block;
      cursor: pointer;
    }

    input {
      margin-bottom: 10px;
    }
  }

  &:last-child {
    align-items: start;
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
