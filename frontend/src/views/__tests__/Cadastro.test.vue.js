import { mount } from '@vue/test-utils';
import HomeView from '../../views/HomeView.vue'

describe('HomeView', () => {
    it('funcionando', () => {
      const wrapper = mount(HomeView);
      expect(wrapper.exists()).toBe(true);
    });
  });