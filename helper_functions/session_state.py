import streamlit as st

class States():

    """
    States Class for Streamlit Session State Management

    Methods:
    --------
    initialise_state(state_dict)
        Initializes the session state with a dictionary of key-value pairs.

    save_state(state_dict)
        Updates the session state with new or existing key-value pairs.

    binaryswitch(key)
        Toggles a boolean key in the session state between True and False.

    clear_output()
        Clears all the session state variables.
    """

    def initialise_state(self, state_dict):
        """
        Initializes the session state with a dictionary of key-value pairs.

        Parameters
        ----------
        state_dict : dict
            A dictionary with keys as state variable names and values as initial values.

        Usage
        -----
        This method is used to set initial state variables within the Streamlit session.
        If a key is already present in the session state, it retains the existing value.
        If not, it initializes the variable with the provided value.
        """
        for k,v in state_dict.items():
            if k not in st.session_state:
                st.session_state[k] = v
            else:
                pass

    def save_state(self, state_dict):
        """
        Updates the session state with new or existing key-value pairs.

        Parameters
        ----------
        state_dict : dict
            A dictionary with keys as state variable names and values as the desired values.

        Usage
        -----
        This method allows updating the state variables within the Streamlit session.
        It overwrites the existing value if the key already exists, otherwise creates a new key-value pair in the session state.
        """
        for k,v in state_dict.items():
            st.session_state[k] = v
    
    def binaryswitch(self, key):
        """
        Toggles a boolean key in the session state between True and False.

        Parameters
        ----------
        key : str
            The key name (representing a boolean state variable) in the session state.

        Usage
        -----
        This method is used to toggle boolean state variables.
        If the key exists and its value is True, it changes it to False, and vice versa.
        """
        if st.session_state[key] is True:
            st.session_state[key] = False
        else:
            st.session_state[key] = True

    def clear_output(self):
        """
        Clears all the session state variables.

        Usage
        -----
        This method removes all state variables currently stored in the Streamlit session.
        """
        for k in st.session_state:
            del st.session_state[k]
ss = States()