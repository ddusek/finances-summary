import React, { useContext } from 'react';
import styled from 'styled-components';
import { ResponsivityContext } from '../../context/Responsivity';
import { UserContext } from '../../context/User';
import { MenuItem } from '../../interfaces';
import { Hamburger } from './Hamburger';
import { NavigationMenu } from './NavigationMenu';

export const Navigation = () => {
  const responsivity = useContext(ResponsivityContext);
  const user = useContext(UserContext);

  const getItems = () => {
    let items: MenuItem[] = [
      { link: '/global-stocks', text: 'Global stocks', highlight: false },
    ];
    user.loggedIn &&
      items.push({ link: '/my-stocks', text: 'My stocks', highlight: false });
    !user.loggedIn &&
      items.push({ link: '/sign-up', text: 'Sign up', highlight: true });
    user.loggedIn &&
      items.push({
        link: '/list-commodities',
        text: 'List commodities',
        highlight: false,
      });
    return items;
  };

  const items = getItems();
  if (responsivity.isMobile) {
    return <Hamburger items={items} />;
  }
  return <NavigationMenu items={items} />;
};
