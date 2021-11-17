import React from 'react';
import styled from 'styled-components';
import { MenuItem } from '../../interfaces';
import { COLOR_DARK } from '../../utils/cssConstants';
import { HamburgerMenuItem } from './HamburgerMenuItem';

const Menu = styled.div`
  display: flex;
  flex-direction: column;
  position: absolute;
  background-color: ${COLOR_DARK};
  top: 59px;
  right: 0;
  padding: 10px 20px;
  border-radius: 0 0 0 5px;
  z-index: 100;
`;

export const HamburgerMenu = (props: { items: MenuItem[] }) => {
  return (
    <Menu>
      {props.items.map((item, i) => {
        return (
          <HamburgerMenuItem
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
