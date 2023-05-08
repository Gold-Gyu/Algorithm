<template>
  <div class="menu-list">
    <h1>3. 옵션을 고르세요.</h1>
    <!-- <ul class="option-list"> -->
    <OptionListItem
    v-for="option in optionList"
    :key="option.id"
    :option="option"
    />
    <!-- </ul> -->
  </div>
</template>

<script>
import OptionListItem from "@/components/OptionListItem.vue"

export default {
  name: 'OptionList',
  components: {
    OptionListItem
  },
  computed: {
    optionList: function () {
      return this.$store.state.optionList
    },
  },
  methods: {
    increase: function () {
    },
    decrease: function () {
    },
  },
}
</script>

<style>
</style>