<template>
  <div :class="{'container':true, 'red-background': favSelected}">
    <div @click="toggleFavourite" :class="{ 'selected': favSelected, 'unselected': !favSelected }"/>
  </div>
</template>

<script>
export default {
  data() {
    return{
      favSelected: false,
    }
  }, 
  props: ['motion'],
  methods: {
    toggleFavourite: async function () {
      this.favSelected = !this.favSelected;
      this.favSelected ? await this.$store.dispatch('postFavorite', { motion: this.motion }) : await this.$store.dispatch('deleteFavorite', { motion: this.motion })
    }
  },
  async created() {
    const userFavorites = (await this.$store.dispatch('getFavorites', {}))
    this.favSelected = userFavorites.filter(favorite => favorite.motion == this.motion).length > 0 ? true : false
  } 
}
</script>

<style scoped lang="scss">
  .selected {
    background-image: url('../assets/favourite-selected.svg');
    height: 37px;
    width: 34px;
    background-size: 37px 34px;
    background-position: center;
    background-repeat: no-repeat;
    cursor:pointer;
    background-color: #ff2b62;

  }
  .unselected {
    background-image: url('../assets/favourite.svg');
    height: 37px;
    width: 34px;
    background-size: 37px 34px;
    background-position: center;
    background-repeat: no-repeat;
    cursor:pointer;

  }

  .container {
    display: flex;
    flex-direction: column;
    width: 75px;
    height: 75px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-right: 20px;
    background-image: linear-gradient(to right, #f5f2e8 0%, #faf9f6 100%);
  }
  .container:hover {
    background-color: #ff2b62;
    background-image: none;

    .unselected {
      background-image: url('../assets/favourite-selected.svg');
      background-color: #ff2b62;
      }

  }
  img {
    cursor: pointer;
    height: 37px;
    width: 34px;
  }
  .red-background {
    background-color: #ff2b62;
    background-image: none;
  }

</style>