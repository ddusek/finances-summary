import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAlignJustify, faTimes } from '@fortawesome/free-solid-svg-icons';
import { HamburgerMenu } from './HamburgerMenu';
import { MenuItem } from '../../interfaces';
import styled from 'styled-components';

const IconContainer = styled.span`
  display: flex;
  margin: auto 20px;
`;

export const Hamburger = (props: { items: MenuItem[] }) => {
  const [showMenu, setShowMenu] = React.useState(false);
  const changeMenuVisibility = () => {
    showMenu ? setShowMenu(false) : setShowMenu(true);
  };
  return (
    <>
      <IconContainer>
        {!showMenu ? (
          <FontAwesomeIcon
            icon={faAlignJustify}
            size="2x"
            onClick={changeMenuVisibility}
          />
        ) : (
          showMenu && (
            <FontAwesomeIcon
              icon={faTimes}
              size="2x"
              onClick={changeMenuVisibility}
            />
          )
        )}
      </IconContainer>
      {showMenu && <HamburgerMenu items={props.items} />}
    </>
  );
};
