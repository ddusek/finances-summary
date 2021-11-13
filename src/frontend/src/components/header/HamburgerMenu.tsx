import React from 'react';
import styled from 'styled-components';
import { MenuItem } from '../../interfaces';
import { HamburgerMenuItem } from './HamburgerMenuItem';

const Menu = styled.div`
  width: 200px;
  height: 300px;
`;

export const HamburgerMenu = (props: { items: MenuItem[] }) => {
  return (
    <Menu>
      {props.items.map((item) => {
        return (
          <HamburgerMenuItem
            highlight={item.highlight}
            link={item.link}
            text={item.text}
          />
        );
      })}
    </Menu>
  );
};
