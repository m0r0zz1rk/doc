<template>
    <tr class="border_bottom">
        <td class="name_req">
            <slot></slot>
        </td>
        <td class="vals_req">
            <slot></slot>
        </td>
        <td class="add_req">
            <slot></slot>
        </td>
    </tr>
</template>

<script>
export default {
    name: 'ListReqs',
}
</script>

<style>
</style>