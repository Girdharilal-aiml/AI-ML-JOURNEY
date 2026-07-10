import streamlit as st
from bank import Bank

bank = Bank()

st.title("🏦 Bank Management System")

option = st.sidebar.selectbox(
    "Menu",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Details",
        "Update Details",
        "Delete Account"
    ]
)

if option == "Create Account":

    st.header("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", step=1)
    email = st.text_input("Email")
    pin = st.number_input("PIN", step=1)

    if st.button("Create"):

        result = bank.create_account(
            name,
            age,
            email,
            int(pin)
        )

        st.success(result)

elif option == "Deposit":

    st.header("Deposit")

    acc = st.number_input("Account Number", step=1)
    pin = st.number_input("PIN", step=1)
    amount = st.number_input("Amount", step=1)

    if st.button("Deposit"):

        msg = bank.deposit(
            int(acc),
            int(pin),
            amount
        )

        st.success(msg)

elif option == "Withdraw":

    acc = st.number_input("Account Number", step=1)
    pin = st.number_input("PIN", step=1)
    amount = st.number_input("Amount", step=1)

    if st.button("Withdraw"):

        st.success(
            bank.withdraw(
                int(acc),
                int(pin),
                amount
            )
        )

elif option == "Details":

    acc = st.number_input("Account Number", step=1)
    pin = st.number_input("PIN", step=1)

    if st.button("Show"):

        user = bank.details(
            int(acc),
            int(pin)
        )

        if user:
            st.json(user)
        else:
            st.error("Account not found")

elif option == "Update Details":

    acc = st.number_input("Account Number", step=1)
    pin = st.number_input("Old PIN", step=1)

    name = st.text_input("New Name")
    email = st.text_input("New Email")
    new_pin = st.number_input("New PIN", step=1)

    if st.button("Update"):

        st.success(
            bank.update_details(
                int(acc),
                int(pin),
                name,
                email,
                int(new_pin)
            )
        )

elif option == "Delete Account":

    acc = st.number_input("Account Number", step=1)
    pin = st.number_input("PIN", step=1)

    if st.button("Delete"):

        st.success(
            bank.delete_account(
                int(acc),
                int(pin)
            )
        )