import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import { MenuItem } from '../../interfaces';
import { COLOR_TEAL } from '../../utils/cssConstants';

const Container = styled.ul`
  margin-right: 15px;
  font-size: 22px;
`;

const Normal = styled.li`
  border: 2px transparent solid;
  display: block;
  position: relative;
  padding: 0.2em 0;
  :after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 0.1em;
    background-color: ${COLOR_TEAL};
    opacity: 0;
    transition: opacity 300ms, transform 300ms;
  }
  ::after {
    opacity: 1;
    transform: scale(0);
    transform-origin: center;
  }
  :hover::after,
  :focus::after {
    transform: scale(1);
  }
`;

const Highlight = styled(Normal)`
  font-weight: 500;
`;

const HighlightItem: React.FC<MenuItem> = (
  props: MenuItem
) => {
  return (
    <Highlight> 
      <Link to={props.link}>{props.text}</Link>
    </Highlight>
  );
};

const NormalItem: React.FC<MenuItem> = (
  props: MenuItem
) => {
  return (
    <Normal>
      <Link to={props.link}>{props.text}</Link>
    </Normal>
  );
};

const NavigationMenuItem: React.FC<MenuItem> = (
  props: MenuItem
) => {
  return (
    <Container>
      {props.highlight ? HighlightItem(props) : NormalItem(props)}
    </Container>
  );
};

export default NavigationMenuItem;
