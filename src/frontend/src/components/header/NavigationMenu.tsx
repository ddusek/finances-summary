import React from 'react';
import styled from 'styled-components';
import { MenuItem } from '../../interfaces';
import NavigationMenuItem from './NavigationMenuItem';

const Menu = styled.nav`
  display: flex;
  flex-direction: row;
  align-items: center;
`;

export const NavigationMenu = (props: { items: MenuItem[] }) => {
  return (
    <Menu>
      {props.items.map((item, i) => {
        return (
          <NavigationMenuItem
            key={i}
            highlight={item.highlight}
            link={item.link}
            text={item.text}
          />
        );
      })}
    </Menu>
  );
};
