import {Modal} from "bootstrap";

const hideModal = (modalEl: HTMLElement | null | string): void => {
    if (!modalEl) {
        return;
    }

    const myModal = typeof modalEl === 'string' ?
        Modal.getInstance(document.getElementById(modalEl)) :
        Modal.getInstance(modalEl);

    myModal?.hide();
};

const displayModal = (id) => {
  const modalObj = new Modal(document.getElementById(id));
    modalObj?.show();
}

const removeModalBackdrop = (): void => {
    if (document.querySelectorAll(".modal-backdrop.fade.show").length) {
        document.querySelectorAll(".modal-backdrop.fade.show").forEach((item) => {
            item.remove();
        });
    }
};

export {removeModalBackdrop, hideModal, displayModal};
