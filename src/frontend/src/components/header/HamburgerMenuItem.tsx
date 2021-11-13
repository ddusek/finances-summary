import React from 'react';
import styled from 'styled-components';
import { MenuItem } from '../../interfaces';

const Normal = styled.span`
  width: 200px;
  height: 50px;
`;
const Highlight = styled.span`
  width: 200px;
  height: 50px;
`;

const Item = (props: MenuItem) => {
  return (
    <Normal>
      <a href={props.link}>{props.text}</a>
    </Normal>
  );
};

const HighlightItem = (props: MenuItem) => {
  return (
    <Highlight>
      <a href={props.link}>{props.text}</a>
    </Highlight>
  );
};

export const HamburgerMenuItem = (
  props: MenuItem
) => {
  return props.highlight ? HighlightItem(props) : Item(props);
};
